from app.repositories.message_repository import MessageRepository

class MessageService:
    def __init__(self):
        self.repository = MessageRepository()

    def process_message(self, message: str) -> str:
        if not message:
            return "Mensagem vazia"
        self.repository.save(message)
        return f"Você disse: {message}"

    def list_messages(self) -> dict:
        return {
                    "data": {
                        "messages": [
                            message for message in self.repository.list()
                        ]
                    }
                }

