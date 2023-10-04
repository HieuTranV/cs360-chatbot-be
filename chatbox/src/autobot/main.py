from fastapi import APIRouter
from master.models import Request, Response
from .models import Message
from .processing import getChatEngine
router = APIRouter(prefix='/autobot')
@router.post("/get-response", response_model=Response[Message])
async def api_get_response(request: Request[Message]):
  chat_engine = getChatEngine(request.request_data.owner_id)
  res = chat_engine.chat(message=request.request_data.content)
  res = Message(content=res.response, owner_id=0, role="assistant")
  return Response(response_data=res)