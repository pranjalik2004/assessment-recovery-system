import time
from app.core.logger import logger


# ✅ Generic retry function
def retry_operation(func, retries=3, delay=1):
    """
    Retries a function if it fails.

    :param func: function to execute
    :param retries: number of retry attempts
    :param delay: delay between retries (seconds)
    """

    for attempt in range(1, retries + 1):
        try:
            result = func()
            logger.info(f"Operation successful on attempt {attempt}")
            return result

        except Exception as e:
            logger.error(f"Attempt {attempt} failed: {str(e)}")

            if attempt < retries:
                time.sleep(delay)

    logger.critical("All retry attempts failed")

    return {
        "status": "failed",
        "message": "Operation failed after multiple retries"
    }
