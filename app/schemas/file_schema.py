from pydantic import BaseModel

class CreateFile(BaseModel):
    filename: str


class EditFile(BaseModel):
    content: str