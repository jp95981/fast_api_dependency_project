from dependency_injector.wiring import Provide
from dependency_injector.wiring import inject
from fastapi import Depends

from fast_api_dependecy_injection.clients.db_client import DBClient
from fast_api_dependecy_injection.containers import Container
from fast_api_dependecy_injection.handlers.handler import HandlerName
from fast_api_dependecy_injection.routers.generate_router import create_task_router
from fast_api_dependecy_injection.schemas.encoder_bisector import EncoderBisectorJobArgs

encoder_router = create_task_router(
    task_name=HandlerName.ENCODER_BISECTOR,
    prefix="/encoder_bisector",
    tags=["encoder_bisector"],
    request_model=EncoderBisectorJobArgs
)


@encoder_router.get("/running-job-for-profile")
@inject
def get_running_job_for_profile(
        job_args: EncoderBisectorJobArgs,
        db_client: DBClient = Depends(Provide[Container.db_client])
):
    # Lookup for running job in the DB
    return db_client.ping()
