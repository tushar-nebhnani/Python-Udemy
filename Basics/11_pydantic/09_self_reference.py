from pydantic import BaseModel
from typing import List, Optional

# Self referencing model
class Comment(BaseModel):
    id: int
    content: str
    replies: Optional[List['Comment']] = None # forward references

Comment.model_rebuild() 

commet = Comment(
    id=1,
    content="First comment",
    replies=[
        Comment(id=2, content="reply 1"),
        Comment(id=3, content="reply 2", replies = [
            Comment(
                id=5, content="Nested Reply"
            )
        ]),
        Comment(id=4, content="reply 3")
    ]
)