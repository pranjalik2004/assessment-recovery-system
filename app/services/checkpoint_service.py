from sqlalchemy.orm import Session
from app.db.models import Checkpoint
from app.core.logger import logger



# ✅ Save checkpoint (called during assessment)
def save_checkpoint(db: Session, data):
    try:
        checkpoint = Checkpoint(
            user_id=data.user_id,
            answers=data.answers,
            current_question=data.current_question
        )

        db.add(checkpoint)
        db.commit()
        db.refresh(checkpoint)

        logger.info(f"Checkpoint saved for user {data.user_id}")

        return {
            "status": "success",
            "message": "Checkpoint saved successfully"
        }

    except Exception as e:
        db.rollback()
        logger.error(f"Error saving checkpoint for user {data.user_id}: {str(e)}")

        return {
            "status": "error",
            "message": "Failed to save checkpoint"
        }


# ✅ Get latest checkpoint (used in recovery)
def get_latest_checkpoint(db: Session, user_id: int):
    try:
        checkpoint = (
            db.query(Checkpoint)
            .filter(Checkpoint.user_id == user_id)
            .order_by(Checkpoint.timestamp.desc())
            .first()
        )

        if checkpoint:
            logger.info(f"Checkpoint fetched for user {user_id}")
        else:
            logger.warning(f"No checkpoint found for user {user_id}")

        return checkpoint

    except Exception as e:
        logger.error(f"Error fetching checkpoint for user {user_id}: {str(e)}")
        return None
