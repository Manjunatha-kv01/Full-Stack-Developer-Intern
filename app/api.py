from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app import schemas, crud

router = APIRouter()

@router.post("/itineraries", response_model=schemas.ItineraryOut)
def create_itinerary(itinerary: schemas.ItineraryCreate, db: Session = Depends(get_db)):
    return crud.create_itinerary(db, itinerary)

@router.get("/itineraries/{itinerary_id}", response_model=schemas.ItineraryOut)
def get_itinerary(itinerary_id: int, db: Session = Depends(get_db)):
    db_itinerary = crud.get_itinerary(db, itinerary_id)
    if not db_itinerary:
        raise HTTPException(status_code=404, detail="Itinerary not found")
    return db_itinerary
