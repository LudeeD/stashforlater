"""
Queue API endpoints for asynchronous image processing.
"""
import logging
from fastapi import APIRouter, HTTPException
from redis import Redis
from rq import Queue

from app.core.config import settings
from app.models.queue import QueueRequest, QueueResponse
from app.jobs.demo import process_image_url

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/queue", tags=["queue"])

# Create Redis connection and queue
redis_conn = Redis(
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT,
    db=settings.REDIS_DB,
    password=settings.REDIS_PASSWORD,
    decode_responses=True,
)
task_queue = Queue("image_processing", connection=redis_conn)


@router.post("/", response_model=QueueResponse)
async def queue_image_processing(request: QueueRequest) -> QueueResponse:
    print("here")
    """
    Queue an image URL for asynchronous processing.

    Args:
        request: QueueRequest containing the image URL

    Returns:
        QueueResponse with success status and job ID
    """
    try:
        # Enqueue the job
        job_instance = task_queue.enqueue(process_image_url, str(request.url))

        logger.info(f"Enqueued image processing job {job_instance.id} for URL: {request.url}")

        return QueueResponse(
            success=True,
            message="Job enqueued successfully",
            job_id=job_instance.id
        )

    except Exception as e:
        logger.error(f"Failed to queue image processing: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Failed to queue image processing: {str(e)}"
        )
