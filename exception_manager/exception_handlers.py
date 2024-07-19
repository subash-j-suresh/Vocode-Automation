from functools import wraps
import logging
from quart import jsonify

from loggers.slack_logger import get_slack_logger

logger = get_slack_logger()


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
            logger.log(level=logging.ERROR, msg=str(e))
            return jsonify(response), 500

    return wrapper
