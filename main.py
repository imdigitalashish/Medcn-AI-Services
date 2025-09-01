import uvicorn


uvicorn.run(
    app="core.server:app",
    reload=True,
    port=8081
)