from fastapi import FastAPI
from view.hello import router as router_hello

app = FastAPI()
app.include_router(router_hello)


@app.get("/ping/", status_code=200)
async def root():
    return {"message": "pong"}

