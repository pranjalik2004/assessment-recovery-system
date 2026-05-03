from app.services.checkpoint_service import get_latest_checkpoint
from app.core.logger import logger



# ✅ Validate checkpoint data (detect partial/corrupted data)
def validate_checkpoint(checkpoint):
    try:
        answers = checkpoint.answers
        current_q = checkpoint.current_question

        # Expected: answers count should match current_question - 1
        if len(answers) < current_q - 1:
            return False

        return True

    except Exception as e:
        logger.error(f"Validation error: {str(e)}")
        return False


# ✅ Main recovery function
def recover_assessment(db, user_id: int):
    try:
        checkpoint = get_latest_checkpoint(db, user_id)

        # ❌ No data found
        if not checkpoint:
            logger.warning(f"No checkpoint found for user {user_id}")

            return {
                "status": "no_recovery",
                "message": "No previous data found"
            }

        # ⚠️ Partial / corrupted data
        if not validate_checkpoint(checkpoint):
            logger.warning(f"Partial data detected for user {user_id}")

            safe_answers = checkpoint.answers
            corrected_question = len(safe_answers) + 1

            return {
                "status": "partial_recovery",
                "message": "Recovered last consistent state",
                "data": {
                    "answers": safe_answers,
                    "current_question": corrected_question
                }
            }

        # ✅ Full recovery
        logger.info(f"Full recovery successful for user {user_id}")

        return {
            "status": "full_recovery",
            "message": "Recovery successful",
            "data": {
                "answers": checkpoint.answers,
                "current_question": checkpoint.current_question
            }
        }

    except Exception as e:
        logger.error(f"Recovery failed for user {user_id}: {str(e)}")

        return {
            "status": "error",
            "message": "Recovery failed due to system error"
        }
