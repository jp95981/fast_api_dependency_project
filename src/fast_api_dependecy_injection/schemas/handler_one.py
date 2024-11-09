from pydantic import BaseModel


class HandlerOneJobArgs(BaseModel):
    profile: str
