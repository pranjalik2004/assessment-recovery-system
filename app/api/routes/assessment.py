from fastapi import APIRouter, Depends, BackgroundTasks
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.assessment_schema import AssessmentSchema
from app.services import checkpoint_service, recovery_service, retry_service

router = APIRouter()


# ✅ Save checkpoint (runs in background)
@router.post("/checkpoint")
def save_checkpoint(
    data: AssessmentSchema,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db)
):
    try:
        # Run checkpoint save in background (non-blocking)
        background_tasks.add_task(checkpoint_service.save_checkpoint, db, data)

        return {
            "status": "processing",
            "message": "Checkpoint saving in background"
        }

    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to initiate checkpoint save: {str(e)}"
        }


# ✅ Recover assessment (with retry logic)
@router.get("/recover/{user_id}")
def recover_assessment(user_id: int, db: Session = Depends(get_db)):
    try:
        # Wrap recovery with retry
        result = retry_service.retry_operation(
            lambda: recovery_service.recover_assessment(db, user_id)
        )

        return result

    except Exception as e:
        return {
            "status": "error",
            "message": f"Recovery failed: {str(e)}"
        }


# ✅ Health check endpoint (useful for testing)
@router.get("/health")
def health_check():
    return {
        "status": "ok",
        "message": "Assessment Recovery System is running"
    }
