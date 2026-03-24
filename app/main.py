from fastapi import FastAPI
from app.controllers.message_controller import router as message_router

app = FastAPI()

app.include_router(message_router)
