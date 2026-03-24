from app.services.message_service import MessageService

def test_process_message():
    service = MessageService()

    result = service.process_message("oi")

    assert result == "Você disse: oi"


def test_process_empty_message():
    service = MessageService()

    result = service.process_message("")

    assert result == "Mensagem vazia"
