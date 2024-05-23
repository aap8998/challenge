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
                            }
                        }
                    }
                }
            }
        }
    }

    app.openapi_schema = openapi_schema
    return app.openapi_schema
