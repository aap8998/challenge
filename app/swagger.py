from fastapi.openapi.utils import get_openapi
from fastapi import FastAPI


def custom_openapi(app: FastAPI):
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Challenge Docs",
        version="1.0.0",
        description="OpenAPI schemas",
        routes=app.routes,
    )
    openapi_schema["paths"]["/graphql"] = {
        "post": {
            "summary": "GraphQL API",
            "operationId": "graphql_post",
            "requestBody": {
                "content": {
                    "application/json": {
                        "schema": {
                            "$ref": "#/components/schemas/Item"
                        },
                        "example": {
                            "query": "{ items { id_tie_fecha_valor } }"
                        }
                    }
                },
                "required": True
            },
            "responses": {
                "200": {
                    "description": "Successful Response",
                    "content": {
                        "application/json": {
                            "schema": {
                                "$ref": "#/components/schemas/Item"
                            },
                            "example": {
                                "data": {
                                    "items": [
                                        {
                                            "id_tie_fecha_valor": 1
                                        }
                                    ]
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    if "components" not in openapi_schema:
        openapi_schema["components"] = {"schemas": {}}
    openapi_schema["components"]["schemas"]["Item"] = {
        "type": "object",
        "properties": {
            "id_tie_fecha_valor": {"type": "integer"},
            "id_cli_cliente": {"type": "number"},
            "id_ga_vista": {"type": "number"},
            "id_ga_tipo_dispositivo": {"type": "number"},
            "id_ga_fuente_medio": {"type": "integer"},
            "desc_ga_sku_producto": {"type": "string"},
            "desc_ga_categoria_producto": {"type": "number"},
            "fc_agregado_carrito_cant": {"type": "integer"},
            "fc_ingreso_producto_monto": {"type": "number"},
            "fc_retirado_carrito_cant": {"type": "number"},
            "fc_detalle_producto_cant": {"type": "integer"},
            "fc_producto_cant": {"type": "integer"},
            "desc_ga_nombre_producto": {"type": "number"},
            "fc_visualizaciones_pag_cant": {"type": "number"},
            "flag_pipol": {"type": "integer"},
            "SASASA": {"type": "string"},
            "id_ga_producto": {"type": "number"},
            "desc_ga_nombre_producto_1": {"type": "string"},
            "desc_ga_sku_producto_1": {"type": "string"},
            "desc_ga_marca_producto": {"type": "string"},
            "desc_ga_cod_producto": {"type": "number"},
            "desc_categoria_producto": {"type": "string"},
            "desc_categoria_prod_principal": {"type": "string"},
        }
    }

    app.openapi_schema = openapi_schema
    return app.openapi_schema
