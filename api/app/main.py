from fastapi import FastAPI
from app.core.exceptions import registrar_handler
from app.controllers.usuario_controller import router as usuario_router


app = FastAPI()

#Traduz as esseções de dominio(app/core/exceptions.py) para resposta HTTP padronizadas
registrar_handler(app)

app.include_router(usuario_router)

# Executar
# uvicorn app.main:app --reload
# Chrome: localhost:8000/docs