from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.datastructures import CommaSeparatedStrings

from src.core import event
from src.core.config import log, settings
from src.endpoints.v1.router_v1 import api_router



def get_application():
    """
    Get FastAPI Application for service.
    """

    app = FastAPI(title=settings.project_name, version=settings.version)

    if not settings.allowed_hosts:
        ALLOWED_HOSTS = ["*"]
    else:
        ALLOWED_HOSTS = CommaSeparatedStrings(settings.allowed_hosts)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=ALLOWED_HOSTS,
        allow_methods=["*"],
        allow_headers=["*"],
        allow_credentials=True,
    )
    

    app.add_event_handler("startup", event.create_start_app_handler(app))
    app.add_event_handler("shutdown", event.create_stop_app_handler(app))
    app.include_router(api_router, prefix=f"{settings.api_prefix }/v1")

    return app


app = get_application()


@app.get("/", description="***** Liveliness Check *****")
async def root():
    """Root API for Service testing.
    Returns:
        obj: Response Obj (Application Declaratives)
    """
    log.info("Test Root API to check server running status.")
    response_dict = {
        "message": "service is active",
        "project": settings.project_name,
        "version": settings.version,
        "production_mode": not settings.debug,
        "documentation": f"{ settings.root_url }{ settings.docs_prefix }",
        "api_endpoint": f"{ settings.root_url }{ settings.api_prefix }",
        "contact_email": settings.admin_email
    }
    return response_dict
