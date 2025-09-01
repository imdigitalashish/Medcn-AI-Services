from fastapi import FastAPI


def create_app() -> FastAPI:
    app = FastAPI(
        title="Medcn AI Services",
    )
    return app


app = create_app()