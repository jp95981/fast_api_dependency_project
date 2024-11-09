from fast_api_dependecy_injection.handlers.handler import Handler
from fast_api_dependecy_injection.schemas.handler_one import HandlerOneJobArgs


class HandlerOne(Handler):
    def create_script(self, job_args: HandlerOneJobArgs):
        return f"handler one: {job_args}"
