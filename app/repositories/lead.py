from collections.abc import Sequence

from app.models.lead import Lead


class LeadRepository:
    """Repository for lead data."""

    def __init__(self) -> None:
        self._leads = [Lead(id=i, name=f"Lead {i}") for i in range(1, 51)]

    def list_leads(self, *, page: int, size: int) -> Sequence[Lead]:
        """Return a slice of leads for the requested page."""
        start = (page - 1) * size
        end = start + size
        return self._leads[start:end]
