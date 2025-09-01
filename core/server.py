from fastapi import FastAPI
from api import router
from dotenv import load_dotenv


load_dotenv()

def create_app() -> FastAPI:
    app = FastAPI(
        title="Medcn AI Services",
    )
    app.include_router(router, prefix="/api")
    return app


app = create_app()