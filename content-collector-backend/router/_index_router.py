from fastapi import APIRouter

from . import note_router

root = APIRouter(prefix="/api/v1")

root.include_router(note_router.api)
