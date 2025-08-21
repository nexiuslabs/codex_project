from fastapi import APIRouter, Depends, Query

from app.models.lead import Lead
from app.repositories.lead import LeadRepository
from app.dependencies import get_lead_repository

router = APIRouter()


@router.get("/leads", response_model=list[Lead], summary="List leads with pagination")
def read_leads(
    *,
    page: int = Query(1, ge=1),
    size: int = Query(10, ge=1, le=100),
    repository: LeadRepository = Depends(get_lead_repository),
) -> list[Lead]:
    """Retrieve leads using simple pagination."""
    return list(repository.list_leads(page=page, size=size))
