# This file is intentionally left blank.from sqlalchemy.orm import Session
from app import models
from app.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

def seed():
    db: Session = SessionLocal()
    phuket_hotel = models.Hotel(name="Seaview Resort", location="Phuket")
    krabi_hotel = models.Hotel(name="Cliffside Retreat", location="Krabi")

    db.add_all([phuket_hotel, krabi_hotel])
    db.commit()

    for nights in range(2, 9):
        itinerary = models.Itinerary(name=f"{nights}-Night Trip", nights=nights)
        db.add(itinerary)
        db.commit()
        db.refresh(itinerary)

        for day in range(1, nights + 1):
            hotel = phuket_hotel if day <= nights // 2 else krabi_hotel
            itinerary_day = models.ItineraryDay(day_number=day, itinerary_id=itinerary.id, hotel_id=hotel.id)
            db.add(itinerary_day)
            db.commit()
            db.refresh(itinerary_day)

            transfer = models.Transfer(day_id=itinerary_day.id, from_location="Phuket", to_location="Krabi", mode="Ferry")
            activity = models.Activity(day_id=itinerary_day.id, name=f"Day {day} Adventure", description="Beach, food, and fun")

            db.add_all([transfer, activity])
            db.commit()

    db.close()

if __name__ == "__main__":
    seed()