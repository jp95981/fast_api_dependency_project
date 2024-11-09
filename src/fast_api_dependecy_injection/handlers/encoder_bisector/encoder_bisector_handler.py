from fast_api_dependecy_injection.handlers.handler import Handler
from fast_api_dependecy_injection.schemas.encoder_bisector import EncoderBisectorJobArgs


class EncoderBisectorHandler(Handler):
    def create_script(self, job_args: EncoderBisectorJobArgs):
        return f"encoder bisector handler: {job_args}"
