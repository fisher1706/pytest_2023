from pydantic import BaseModel, Field

"""
all class inherited from BaseModel
"""


class Post(BaseModel):
    id: int = Field(le=4)
    title: str


data_of_validation = {
    'id': 1,
    'title': 'Post 1'
}
