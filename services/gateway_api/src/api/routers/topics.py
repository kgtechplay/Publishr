from fastapi import APIRouter
router = APIRouter(prefix='/topics', tags=['topics'])

@router.get('')
def list_topics():
    return []
