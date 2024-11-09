from typing import Dict

from fast_api_dependecy_injection.handlers import EncoderBisectorHandler, HandlerOne, HandlerName, Handler


class HandlerFactory:
    handlers: Dict[HandlerName, Handler] = {
        HandlerName.ENCODER_BISECTOR: EncoderBisectorHandler,
        HandlerName.ANOTHER_HANDLER_ONE: HandlerOne,
    }

    def create_handler(self, handler: HandlerName):
        found_handler = self.handlers.get(handler, None)
        if found_handler:
            return found_handler()
        raise ValueError(f"Handler '{handler}' not implemented!")
