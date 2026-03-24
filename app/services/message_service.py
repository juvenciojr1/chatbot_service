class MessageService:

    def process_message(self, message: str) -> str:
        if not message:
            return "Mensagem vazia"

        return f"Você disse: {message}"
