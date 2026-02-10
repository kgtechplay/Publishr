from fastapi import APIRouter
router = APIRouter(prefix='/commands', tags=['commands'])

@router.post('/runs')
def start_run():
    return {'status': 'accepted'}
