from fastapi import APIRouter
from app.schemas.message_schema import MessageRequest, MessageResponse
from app.services.message_service import MessageService

router = APIRouter(prefix="/messages", tags=["messages"])

service = MessageService()

@router.post("/")
def send_message(request: MessageRequest) -> MessageResponse:
    response = service.process_message(request.message)
    return MessageResponse(response=response)

@router.get("/")
def list_messages() -> dict:
    return service.list_messages()

