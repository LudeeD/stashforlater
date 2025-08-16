import redis
from rq import Queue

from app.core.config import settings


def get_redis_connection() -> redis.Redis:
    """Get Redis connection instance."""
    return redis.Redis(
        host=settings.REDIS_HOST,
        port=settings.REDIS_PORT,
        db=settings.REDIS_DB,
        password=settings.REDIS_PASSWORD,
        decode_responses=True,
    )


def get_queue() -> Queue:
    """Get RQ queue instance."""
    redis_conn = get_redis_connection()
    return Queue("image_processing", connection=redis_conn)