# Full-Stack-Developer-Intern
Create a backend system for managing travel itineraries with the following components: 1. Database architecture for trip itineraries and models for the same using SQLAlchemy 2. RESTful API endpoints for creating and viewing itineraries 3. MCP server that provides recommended itineraries based on duration


Detailed Requirements
1. Database Architecture
● Design and implement the database schema using SQLAlchemy
● Your schema should support:
○ Day-wise hotel accommodations, transfers between locations,
activities/excursions
○ Relationship between these entities
● Seed the database with realistic data for the Phuket and Krabi regions in Thailand
● Include recommended itineraries ranging from 2-8 nights
● Implement proper relationships, constraints, and indexes
2. API Endpoints
● Create RESTful API endpoints using FastAPI that allows:
○ Creating a new trip itinerary
○ Viewing existing trip itineraries
● Implement proper input validation, error handling, and response formatting
● Document the API with sample request/response formats
3. MCP Server
● Implement an MCP server that returns recommended itineraries for given number of
nights
