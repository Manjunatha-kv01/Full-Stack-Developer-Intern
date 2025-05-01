from fastapi import FastAPI
from app.api import router as api_router
from app.mcp_server import router as mcp_router
from app.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Travel Itinerary Backend")

app.include_router(api_router, prefix="/api")
app.include_router(mcp_router, prefix="/api")
