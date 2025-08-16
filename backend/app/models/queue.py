"""
Pydantic models for queue operations.
"""
from pydantic import BaseModel, HttpUrl


class QueueRequest(BaseModel):
    """Request model for queueing image processing tasks."""
    url: HttpUrl


class QueueResponse(BaseModel):
    """Response model for queue operations."""
    success: bool
    message: str
    job_id: str | None = None