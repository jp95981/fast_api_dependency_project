from fastapi import FastAPI

from fast_api_dependecy_injection.containers import Container
from fast_api_dependecy_injection.routers import encoder_router, handler_one_router, router


def create_app():
    container = Container()

    # container.db_client()
    # jira_session = container.jira_client()
    # gitlab_session = container.gitlab_client()

    app = FastAPI()
    app.container = container
    app.include_router(encoder_router)
    app.include_router(handler_one_router)
    app.include_router(router)

    return app


app = create_app()


@app.get("/")
async def root():
    return {"message": "Hello World"}
