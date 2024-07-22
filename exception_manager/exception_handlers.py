from functools import wraps
from loggers.application_logger import logger
from quart import jsonify


def webhook_exception_handler(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except Exception as e:
            response = {
                "error": str(e),
                "message": "An error occurred. Please try again later.",
            }
            logger.error(msg=str(e))
            return jsonify(response), 500

    return wrapper
