from fastapi import FastAPI

from app.db.database import Base, engine

from app.api.routes import assessment

# Create FastAPI app
app = FastAPI(
    title="Assessment Failure Recovery System",
    description="Handles API crash recovery and partial data recovery",
    version="1.0.0"
)

# Create database tables
Base.metadata.create_all(bind=engine)

# Include routes
app.include_router(
    assessment.router,
    prefix="/assessment",
    tags=["Assessment Recovery"]
)


# Root endpoint
@app.get("/")
def home():
    return {
        "message": "Assessment Recovery System Running"
    }
