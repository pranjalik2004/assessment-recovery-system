from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import DATABASE_URL

# 👉 Replace with your actual PostgreSQL credentials

# Create database engine
engine = create_engine(
    DATABASE_URL,
    echo=True  # Shows SQL logs (good for debugging, remove in production)
)

# Create session (used for DB operations)
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Base class for models
Base = declarative_base()


# Dependency (used in FastAPI routes)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
