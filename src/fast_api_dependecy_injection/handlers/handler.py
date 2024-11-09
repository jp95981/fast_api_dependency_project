from abc import ABC, abstractmethod
from enum import Enum, auto

from pydantic import BaseModel


class HandlerName(Enum):
    ENCODER_BISECTOR = auto()
    ANOTHER_HANDLER_ONE = auto()
    ANOTHER_HANDLE_TWO = auto()


class Handler(ABC):
    @abstractmethod
    def create_script(self, job_args: BaseModel):
        raise NotImplementedError()
