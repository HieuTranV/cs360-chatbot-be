from pydantic import BaseModel

class Message(BaseModel):
  content: str
  owner_id: int
  role: str