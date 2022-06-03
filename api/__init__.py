from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import aioredis


def create_app():
    app = FastAPI(
        # change this with your api title
        title="Api Title",
        # change this with your api description
        description="Api description",
        # change this with your api version
        version="APi version",
        # change API_blueprint_name with your api blueprint name
        openapi_url="/api/openapi.json",
        # change API_blueprint_name with your api blueprint name
        docs_url="/api/docs",
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    from .service.routes import router as service_router
    # change API_blueprint_name with your api blueprint name
    app.include_router(service_router, prefix="/api")
    return app


redis = aioredis.from_url(
    "redis://localhost:6379", username="default", password="sec_rEtPass")
app = create_app()
