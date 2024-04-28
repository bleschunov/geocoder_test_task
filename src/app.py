from fastapi import FastAPI
import uvicorn

from dotenv import load_dotenv

load_dotenv()

from controller import geocoder_controller
from infra.db import engine


app = FastAPI()

app.include_router(geocoder_controller.router)


@app.on_event("shutdown")
async def shutdown():
    engine.dispose()


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8080, reload=False)
