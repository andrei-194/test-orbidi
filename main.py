from fastapi import FastAPI
from starlette.responses import RedirectResponse

from routes.sinc import sinc
from routes.user import user

app = FastAPI(
    title="Prueba tecnica",
    version="1.0"
)

app.include_router(user.user_router)
app.include_router(sinc.sync_router)


@app.get("/")
async def main():
    return RedirectResponse(url="/docs/")
