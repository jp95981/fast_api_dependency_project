from fast_api_dependecy_injection.handlers.handler import HandlerName
from fast_api_dependecy_injection.routers.generate_router import create_task_router
from fast_api_dependecy_injection.schemas.handler_one import HandlerOneJobArgs

handler_one_router = create_task_router(
    task_name=HandlerName.ANOTHER_HANDLER_ONE,
    prefix="/handler_one",
    tags=["handler_one"],
    request_model=HandlerOneJobArgs
)
