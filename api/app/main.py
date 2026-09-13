from fastapi import FastAPI
from app.core.config import settings
from app.core.database import engine, SessionLocal
from app.core.tempo import agora

app = FastAPI(
    title="Helpdesk API",
    version="1.0.0",
    description="API de ajuda técnica com FastAPI"
)

@app.get("/")
def root():
    return {"message": "Welcome to Helpdesk API", "status": "running"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
