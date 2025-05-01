from sqlalchemy.orm import Session
from app import models, schemas

def create_itinerary(db: Session, itinerary: schemas.ItineraryCreate):
    db_itinerary = models.Itinerary(name=itinerary.name, nights=itinerary.nights)
    db.add(db_itinerary)
    db.commit()
    db.refresh(db_itinerary)
    return db_itinerary

def get_itinerary(db: Session, itinerary_id: int):
    return db.query(models.Itinerary).filter(models.Itinerary.id == itinerary_id).first()

def get_recommended_itinerary(db: Session, nights: int):
    return db.query(models.Itinerary).filter(models.Itinerary.nights == nights).all()
