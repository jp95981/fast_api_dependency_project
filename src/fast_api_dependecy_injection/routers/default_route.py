from dependency_injector.wiring import inject
from fastapi import APIRouter

router = APIRouter()


@router.get('/job/{job_id}')
@inject
def get_job_status(job_id: int):
    return "Job is running somehow"


@router.delete('/job/{job_id}')
def cancel_job(job_id: int):
    return "job has been cancelled"
