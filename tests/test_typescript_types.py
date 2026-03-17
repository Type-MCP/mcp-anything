"""Tests for TypeScript type extraction in Express.js routes."""

from mcp_anything.analysis.express_analyzer import analyze_express_file
from mcp_anything.models.analysis import FileInfo, Language


def _ts_fi(path: str) -> FileInfo:
    return FileInfo(path=path, language=Language.TYPESCRIPT, size_bytes=500, line_count=40)


class TestTypeScriptTypeExtraction:
    def test_parseInt_infers_integer(self, fake_ts_express_app):
        result = analyze_express_file(fake_ts_express_app, _ts_fi("server.ts"))
        assert result is not None

        get_user = next(r for r in result.routes if r.path == "/users/{id}" and r.http_method == "GET")
        id_param = next(p for p in get_user.parameters if p.name == "id")
        assert id_param.type == "integer"

    def test_as_number_cast_infers_integer(self, fake_ts_express_app):
        result = analyze_express_file(fake_ts_express_app, _ts_fi("server.ts"))

        get_products = next(r for r in result.routes if r.path == "/products" and r.http_method == "GET")
        params_by_name = {p.name: p for p in get_products.parameters}

        assert params_by_name["page"].type == "integer"
        assert params_by_name["limit"].type == "integer"
        assert params_by_name["search"].type == "string"

    def test_typed_destructuring_infers_types(self, fake_ts_express_app):
        result = analyze_express_file(fake_ts_express_app, _ts_fi("server.ts"))

        post_orders = next(r for r in result.routes if r.path == "/orders" and r.http_method == "POST")
        params_by_name = {p.name: p for p in post_orders.parameters}

        assert params_by_name["productId"].type == "string"
        assert params_by_name["quantity"].type == "integer"
        assert params_by_name["price"].type == "integer"

    def test_request_generic_infers_types(self, fake_ts_express_app):
        result = analyze_express_file(fake_ts_express_app, _ts_fi("server.ts"))

        put_item = next(r for r in result.routes if r.path == "/items/{id}" and r.http_method == "PUT")
        params_by_name = {p.name: p for p in put_item.parameters}

        assert params_by_name["name"].type == "string"
        assert params_by_name["active"].type == "boolean"

    def test_plain_js_style_still_works(self, fake_ts_express_app):
        result = analyze_express_file(fake_ts_express_app, _ts_fi("server.ts"))

        delete_item = next(r for r in result.routes if r.path == "/items/{id}" and r.http_method == "DELETE")
        id_param = next(p for p in delete_item.parameters if p.name == "id")
        # No type hint available → falls back to string
        assert id_param.type == "string"
        assert id_param.required is True

    def test_all_routes_detected(self, fake_ts_express_app):
        result = analyze_express_file(fake_ts_express_app, _ts_fi("server.ts"))
        assert result is not None
        assert len(result.routes) == 5
