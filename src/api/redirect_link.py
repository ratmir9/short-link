from fastapi import (
  APIRouter,
  Depends
)
from fastapi.responses import RedirectResponse

from src.services.link.link import LinkService


router = APIRouter()

@router.get('/r/{code}', response_class=RedirectResponse)
def red(
  code: str,
  service: LinkService = Depends()
):
  return service.redirect_code(code)