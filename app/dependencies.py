from app.repositories.lead import LeadRepository


def get_lead_repository() -> LeadRepository:
    """Dependency injection for LeadRepository."""
    return LeadRepository()
