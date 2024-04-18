from fastapi import FastAPI

from jubellos_api.router import router

app = FastAPI(docs_url="/api/v1/docs", redoc_url=None, title="Jubellos API")
app.include_router(router, tags=["scratchTickets"], prefix="/api/v1")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8888)