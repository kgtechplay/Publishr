from fastapi import APIRouter
router = APIRouter(prefix='/assets', tags=['assets'])

@router.get('')
def list_assets():
    return []
