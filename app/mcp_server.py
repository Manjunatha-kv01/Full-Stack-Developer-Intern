from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app import crud

router = APIRouter()

@router.get("/mcp/recommend/{nights}")
def recommend_itinerary(nights: int, db: Session = Depends(get_db)):
    return crud.get_recommended_itinerary(db, nights)
