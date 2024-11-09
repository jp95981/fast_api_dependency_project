from typing import List, Type

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends
from pydantic import BaseModel

from fast_api_dependecy_injection.clients.jira_client import JiraClient
from fast_api_dependecy_injection.containers import Container
from fast_api_dependecy_injection.dependencies import get_handler_factory
from fast_api_dependecy_injection.factories.handler_factory import HandlerFactory
from fast_api_dependecy_injection.handlers import HandlerName


def create_task_router(
        task_name: HandlerName,
        prefix: str,
        tags: List[str],
        request_model: Type[BaseModel]
) -> APIRouter:
    """
    Factory function to create a router with a `/job` endpoint.

    :param request_model:
    :param task_name: The HandlerName enum value for the specific task.
    :param prefix: URL prefix for the router.
    :param tags: List of tags for the router.
    :return: Configured APIRouter instance.
    """
    router = APIRouter(prefix=prefix, tags=tags)

    @router.post("/job", summary=f"Submit job for {task_name.value}")
    @inject
    async def submit_job(job_args: request_model, handler_factory: HandlerFactory = Depends(get_handler_factory),
                         jira_client: JiraClient = Depends(Provide[Container.jira_client])):
        handler = handler_factory.create_handler(task_name)
        cmd = handler.create_script(job_args=job_args)
        # job_scheduler.submit(cmd)

        return {"result": f"Job for {task_name.value} submitted successfully. {jira_client.ping()}"}

    return router
