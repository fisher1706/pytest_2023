from pydantic import BaseModel, Field


class Post(BaseModel):
    id: int = Field(le=4)
    title: str
