from fastapi import APIRouter
router = APIRouter(prefix='/publish', tags=['publish'])

@router.post('/{run_id}')
def publish_run(run_id: str):
    return {'run_id': run_id, 'status': 'queued'}
