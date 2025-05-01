from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.database import Base

class Itinerary(Base):
    __tablename__ = "itineraries"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    nights = Column(Integer, nullable=False)

    days = relationship("ItineraryDay", back_populates="itinerary", cascade="all, delete-orphan")

class ItineraryDay(Base):
    __tablename__ = "itinerary_days"
    id = Column(Integer, primary_key=True, index=True)
    itinerary_id = Column(Integer, ForeignKey("itineraries.id"))
    day_number = Column(Integer, nullable=False)

    hotel_id = Column(Integer, ForeignKey("hotels.id"))
    hotel = relationship("Hotel")

    transfers = relationship("Transfer", back_populates="day")
    activities = relationship("Activity", back_populates="day")

    itinerary = relationship("Itinerary", back_populates="days")

class Hotel(Base):
    __tablename__ = "hotels"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)

class Transfer(Base):
    __tablename__ = "transfers"
    id = Column(Integer, primary_key=True, index=True)
    day_id = Column(Integer, ForeignKey("itinerary_days.id"))
    from_location = Column(String)
    to_location = Column(String)
    mode = Column(String)

    day = relationship("ItineraryDay", back_populates="transfers")

class Activity(Base):
    __tablename__ = "activities"
    id = Column(Integer, primary_key=True, index=True)
    day_id = Column(Integer, ForeignKey("itinerary_days.id"))
    name = Column(String)
    description = Column(Text)

    day = relationship("ItineraryDay", back_populates="activities")
