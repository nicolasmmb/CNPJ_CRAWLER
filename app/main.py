from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse

import app.routes as routes

app: FastAPI = FastAPI(
    title="CNPJ API",
    description="API para consulta de CNPJ",
    version="1.0.0",
    contact={
        "name": "Nicolas Barbosa",
        "email": "nicolas.mmb@hotmail.com",
        "url": "https://github.com/nicolasmmb",
    },
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", include_in_schema=False)
async def root() -> RedirectResponse:
    return RedirectResponse(url="/docs")


### Importing routes
app.include_router(routes.cnpj.app, prefix="/api")
