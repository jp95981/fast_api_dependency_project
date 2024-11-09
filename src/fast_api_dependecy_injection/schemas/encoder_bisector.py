from pydantic import BaseModel


class EncoderBisectorJobArgs(BaseModel):
    profile: str
    format: str
    version: str
