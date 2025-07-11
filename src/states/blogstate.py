from typing import TypedDict
from pydantic import BaseModel,Field

class Blog(BaseModel):
    title:str=Field(description="the title of the blog post")
    content:str=Field(description="The main content of the blog post")

class BlogState(TypedDict):
    topic:str
    blog:Blog
    current_language:str
