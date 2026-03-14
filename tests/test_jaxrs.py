"""Tests for JAX-RS and Quarkus support — detector, analyzer, and capabilities."""

from mcp_anything.analysis.detectors.jaxrs_detector import JaxRSDetector
from mcp_anything.analysis.java_analyzer import (
    analyze_java_file,
    java_results_to_capabilities,
)
from mcp_anything.analysis.scanner import scan_codebase
from mcp_anything.models.analysis import FileInfo, IPCType, Language


class TestJaxRSDetector:
    def test_detects_jaxrs(self, fake_jaxrs_app):
        files = scan_codebase(fake_jaxrs_app)
        detector = JaxRSDetector()
        mechanisms = detector.detect(fake_jaxrs_app, files)

        assert len(mechanisms) == 1
        mech = mechanisms[0]
        assert mech.ipc_type == IPCType.PROTOCOL
        assert mech.confidence >= 0.85
        assert mech.details["protocol"] == "http"

    def test_detects_quarkus_framework(self, fake_jaxrs_app):
        files = scan_codebase(fake_jaxrs_app)
        detector = JaxRSDetector()
        mechanisms = detector.detect(fake_jaxrs_app, files)

        # Fixture has quarkus config, so framework should be quarkus
        assert mechanisms[0].details["framework"] == "quarkus"

    def test_detects_port(self, fake_jaxrs_app):
        files = scan_codebase(fake_jaxrs_app)
        detector = JaxRSDetector()
        mechanisms = detector.detect(fake_jaxrs_app, files)

        assert mechanisms[0].details["port"] == "8080"

    def test_finds_jaxrs_evidence(self, fake_jaxrs_app):
        files = scan_codebase(fake_jaxrs_app)
        detector = JaxRSDetector()
        mechanisms = detector.detect(fake_jaxrs_app, files)

        evidence_text = " ".join(mechanisms[0].evidence)
        assert "JAX-RS" in evidence_text
        assert "path annotation" in evidence_text.lower() or "GET" in evidence_text

    def test_no_detection_on_spring(self, fake_spring_app):
        files = scan_codebase(fake_spring_app)
        detector = JaxRSDetector()
        mechanisms = detector.detect(fake_spring_app, files)
        assert mechanisms == []

    def test_no_detection_on_cli(self, fake_cli_app):
        files = scan_codebase(fake_cli_app)
        detector = JaxRSDetector()
        mechanisms = detector.detect(fake_cli_app, files)
        assert mechanisms == []


class TestJaxRSAnalyzer:
    def test_finds_endpoints(self, fake_jaxrs_app):
        fi = FileInfo(
            path="src/main/java/com/example/api/ItemResource.java",
            language=Language.JAVA,
            size_bytes=500,
            line_count=40,
        )
        result = analyze_java_file(fake_jaxrs_app, fi)

        assert result is not None
        assert len(result.endpoints) >= 5
        assert "ItemResource" in result.controllers

    def test_extracts_http_methods(self, fake_jaxrs_app):
        fi = FileInfo(
            path="src/main/java/com/example/api/ItemResource.java",
            language=Language.JAVA,
            size_bytes=500,
            line_count=40,
        )
        result = analyze_java_file(fake_jaxrs_app, fi)

        methods = {ep.http_method for ep in result.endpoints}
        assert "GET" in methods
        assert "POST" in methods
        assert "PUT" in methods
        assert "DELETE" in methods

    def test_extracts_paths(self, fake_jaxrs_app):
        fi = FileInfo(
            path="src/main/java/com/example/api/ItemResource.java",
            language=Language.JAVA,
            size_bytes=500,
            line_count=40,
        )
        result = analyze_java_file(fake_jaxrs_app, fi)

        paths = {ep.path for ep in result.endpoints}
        assert "/api/items" in paths
        assert "/api/items/{id}" in paths

    def test_extracts_path_params(self, fake_jaxrs_app):
        fi = FileInfo(
            path="src/main/java/com/example/api/ItemResource.java",
            language=Language.JAVA,
            size_bytes=500,
            line_count=40,
        )
        result = analyze_java_file(fake_jaxrs_app, fi)

        get_by_id = next(
            ep for ep in result.endpoints
            if ep.method_name == "getItem"
        )
        assert len(get_by_id.parameters) == 1
        assert get_by_id.parameters[0].name == "id"
        assert get_by_id.parameters[0].required is True

    def test_extracts_query_params(self, fake_jaxrs_app):
        fi = FileInfo(
            path="src/main/java/com/example/api/ItemResource.java",
            language=Language.JAVA,
            size_bytes=500,
            line_count=40,
        )
        result = analyze_java_file(fake_jaxrs_app, fi)

        list_items = next(
            ep for ep in result.endpoints
            if ep.method_name == "listItems"
        )
        assert len(list_items.parameters) == 1
        assert list_items.parameters[0].name == "category"
        assert list_items.parameters[0].required is False

    def test_has_no_spring_boot(self, fake_jaxrs_app):
        fi = FileInfo(
            path="src/main/java/com/example/api/ItemResource.java",
            language=Language.JAVA,
            size_bytes=500,
            line_count=40,
        )
        result = analyze_java_file(fake_jaxrs_app, fi)
        assert result.has_spring_boot is False


class TestJaxRSCapabilities:
    def test_endpoints_become_capabilities(self, fake_jaxrs_app):
        fi = FileInfo(
            path="src/main/java/com/example/api/ItemResource.java",
            language=Language.JAVA,
            size_bytes=500,
            line_count=40,
        )
        result = analyze_java_file(fake_jaxrs_app, fi)
        caps = java_results_to_capabilities({fi.path: result})

        assert len(caps) >= 5
        cap_names = [c.name for c in caps]
        assert any("get" in n and "items" in n for n in cap_names)
        assert any("post" in n and "items" in n for n in cap_names)
        assert any("delete" in n and "items" in n for n in cap_names)

    def test_capabilities_have_correct_ipc_type(self, fake_jaxrs_app):
        fi = FileInfo(
            path="src/main/java/com/example/api/ItemResource.java",
            language=Language.JAVA,
            size_bytes=500,
            line_count=40,
        )
        result = analyze_java_file(fake_jaxrs_app, fi)
        caps = java_results_to_capabilities({fi.path: result})

        for cap in caps:
            assert cap.ipc_type == IPCType.PROTOCOL
            assert cap.category == "api"
