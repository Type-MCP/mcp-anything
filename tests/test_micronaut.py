"""Tests for Micronaut support — detector, analyzer, and capabilities."""

from mcp_anything.analysis.detectors.micronaut_detector import MicronautDetector
from mcp_anything.analysis.java_analyzer import (
    analyze_java_file,
    java_results_to_capabilities,
)
from mcp_anything.analysis.scanner import scan_codebase
from mcp_anything.models.analysis import FileInfo, IPCType, Language


class TestMicronautDetector:
    def test_detects_micronaut(self, fake_micronaut_app):
        files = scan_codebase(fake_micronaut_app)
        detector = MicronautDetector()
        mechanisms = detector.detect(fake_micronaut_app, files)

        assert len(mechanisms) == 1
        mech = mechanisms[0]
        assert mech.ipc_type == IPCType.PROTOCOL
        assert mech.confidence >= 0.85
        assert mech.details["protocol"] == "http"
        assert mech.details["framework"] == "micronaut"

    def test_detects_port(self, fake_micronaut_app):
        files = scan_codebase(fake_micronaut_app)
        detector = MicronautDetector()
        mechanisms = detector.detect(fake_micronaut_app, files)

        assert mechanisms[0].details["port"] == "8080"

    def test_finds_micronaut_evidence(self, fake_micronaut_app):
        files = scan_codebase(fake_micronaut_app)
        detector = MicronautDetector()
        mechanisms = detector.detect(fake_micronaut_app, files)

        evidence_text = " ".join(mechanisms[0].evidence)
        assert "Micronaut" in evidence_text

    def test_no_detection_on_spring(self, fake_spring_app):
        files = scan_codebase(fake_spring_app)
        detector = MicronautDetector()
        mechanisms = detector.detect(fake_spring_app, files)
        assert mechanisms == []

    def test_no_detection_on_cli(self, fake_cli_app):
        files = scan_codebase(fake_cli_app)
        detector = MicronautDetector()
        mechanisms = detector.detect(fake_cli_app, files)
        assert mechanisms == []


class TestMicronautAnalyzer:
    def test_finds_endpoints(self, fake_micronaut_app):
        fi = FileInfo(
            path="src/main/java/com/example/api/OrderController.java",
            language=Language.JAVA,
            size_bytes=500,
            line_count=35,
        )
        result = analyze_java_file(fake_micronaut_app, fi)

        assert result is not None
        assert len(result.endpoints) >= 5
        assert "OrderController" in result.controllers

    def test_extracts_http_methods(self, fake_micronaut_app):
        fi = FileInfo(
            path="src/main/java/com/example/api/OrderController.java",
            language=Language.JAVA,
            size_bytes=500,
            line_count=35,
        )
        result = analyze_java_file(fake_micronaut_app, fi)

        methods = {ep.http_method for ep in result.endpoints}
        assert "GET" in methods
        assert "POST" in methods
        assert "PUT" in methods
        assert "DELETE" in methods

    def test_extracts_paths(self, fake_micronaut_app):
        fi = FileInfo(
            path="src/main/java/com/example/api/OrderController.java",
            language=Language.JAVA,
            size_bytes=500,
            line_count=35,
        )
        result = analyze_java_file(fake_micronaut_app, fi)

        paths = {ep.path for ep in result.endpoints}
        assert "/api/orders/" in paths or "/api/orders" in paths
        assert "/api/orders/{id}" in paths

    def test_extracts_path_variable(self, fake_micronaut_app):
        fi = FileInfo(
            path="src/main/java/com/example/api/OrderController.java",
            language=Language.JAVA,
            size_bytes=500,
            line_count=35,
        )
        result = analyze_java_file(fake_micronaut_app, fi)

        get_order = next(
            ep for ep in result.endpoints
            if ep.method_name == "getOrder"
        )
        assert len(get_order.parameters) == 1
        assert get_order.parameters[0].name == "id"
        assert get_order.parameters[0].required is True

    def test_extracts_query_value(self, fake_micronaut_app):
        fi = FileInfo(
            path="src/main/java/com/example/api/OrderController.java",
            language=Language.JAVA,
            size_bytes=500,
            line_count=35,
        )
        result = analyze_java_file(fake_micronaut_app, fi)

        list_orders = next(
            ep for ep in result.endpoints
            if ep.method_name == "listOrders"
        )
        assert len(list_orders.parameters) == 1
        assert list_orders.parameters[0].name == "status"
        assert list_orders.parameters[0].required is False

    def test_extracts_body(self, fake_micronaut_app):
        fi = FileInfo(
            path="src/main/java/com/example/api/OrderController.java",
            language=Language.JAVA,
            size_bytes=500,
            line_count=35,
        )
        result = analyze_java_file(fake_micronaut_app, fi)

        create_order = next(
            ep for ep in result.endpoints
            if ep.method_name == "createOrder"
        )
        body_params = [p for p in create_order.parameters if p.type == "object"]
        assert len(body_params) == 1
        assert body_params[0].required is True

    def test_has_no_spring_boot(self, fake_micronaut_app):
        fi = FileInfo(
            path="src/main/java/com/example/api/OrderController.java",
            language=Language.JAVA,
            size_bytes=500,
            line_count=35,
        )
        result = analyze_java_file(fake_micronaut_app, fi)
        assert result.has_spring_boot is False


class TestMicronautCapabilities:
    def test_endpoints_become_capabilities(self, fake_micronaut_app):
        fi = FileInfo(
            path="src/main/java/com/example/api/OrderController.java",
            language=Language.JAVA,
            size_bytes=500,
            line_count=35,
        )
        result = analyze_java_file(fake_micronaut_app, fi)
        caps = java_results_to_capabilities({fi.path: result})

        assert len(caps) >= 5
        cap_names = [c.name for c in caps]
        assert any("get" in n and "orders" in n for n in cap_names)
        assert any("post" in n and "orders" in n for n in cap_names)
        assert any("delete" in n and "orders" in n for n in cap_names)

    def test_capabilities_have_correct_ipc_type(self, fake_micronaut_app):
        fi = FileInfo(
            path="src/main/java/com/example/api/OrderController.java",
            language=Language.JAVA,
            size_bytes=500,
            line_count=35,
        )
        result = analyze_java_file(fake_micronaut_app, fi)
        caps = java_results_to_capabilities({fi.path: result})

        for cap in caps:
            assert cap.ipc_type == IPCType.PROTOCOL
            assert cap.category == "api"
