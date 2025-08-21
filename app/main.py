from fastapi import FastAPI

from app.routers import leads

app = FastAPI()

app.include_router(leads.router)
