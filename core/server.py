from fastapi import FastAPI
from api import router
from dotenv import load_dotenv

from fastapi.security import OAuth2PasswordBearer
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()

def create_app() -> FastAPI:
    app = FastAPI(
        title="Medcn AI Services",
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=False,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.include_router(router, prefix="/api")
    return app


app = create_app()