from fastapi import APIRouter
router = APIRouter(prefix='/queries', tags=['queries'])

@router.get('/runs/{run_id}')
def get_run(run_id: str):
    return {'run_id': run_id, 'status': 'unknown'}
