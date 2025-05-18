from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import tasks

app = FastAPI(
    title="Task Manager API",
    description="Serviço de gerenciamento de tarefas com autenticação JWT externa.",
    version="1.0.0"
)

# Middleware CORS (permite requisições de outros domínios, como um frontend separado)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Em produção, substitua pelo domínio real do frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Roteador da API de tarefas
app.include_router(tasks.router, prefix="/tasks", tags=["Tarefas"])

# Rota inicial
@app.get("/")
def read_root():
    return {"message": "Task Service API online 🚀"}
