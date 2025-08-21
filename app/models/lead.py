from pydantic import BaseModel, ConfigDict


class Lead(BaseModel):
    """Lead data model."""

    model_config = ConfigDict(extra="forbid")

    id: int
    name: str
