from sqlalchemy import Column, Integer, JSON, DateTime
from datetime import datetime
from app.db.database import Base



class Checkpoint(Base):
    __tablename__ = "checkpoints"

    # Primary Key
    id = Column(Integer, primary_key=True, index=True)

    # User Identifier
    user_id = Column(Integer, index=True, nullable=False)

    # Stores answers in JSON format
    answers = Column(JSON, nullable=False)

    # Current question number
    current_question = Column(Integer, nullable=False)

    # Timestamp of checkpoint
    timestamp = Column(DateTime, default=datetime.utcnow)
