from typing import List

from fastapi import (
  APIRouter,
  Depends,
  status
)
from fastapi.responses import Response


from src.services.link.link import LinkService
from src.models.link import (
  BaseLink, 
  DetailLink
)
from src.models.user import DetailUserJwt
from src.services.user.current_user import get_current_user


router = APIRouter()


@router.get('/', response_model=List[DetailLink])
def list_link(
  service: LinkService = Depends(),
  user: DetailUserJwt = Depends(get_current_user)
):
  return service.get_all_links_user(user_id=user.id)


@router.get('/{id}/')
def detail_link(
  id: int,
  service: LinkService = Depends(),
  user: DetailUserJwt = Depends(get_current_user)
):
  return service.detail_link(
    user_id=user.id,
    link_id=id
  )


@router.post('/', response_model=DetailLink, status_code=status.HTTP_201_CREATED)
def create_short_link(
  link: BaseLink,
  service: LinkService = Depends(),
  user: DetailUserJwt = Depends(get_current_user)
):
  return service.create_link(
    user_id=user.id,
    origin_link=link.origin_link
  )


@router.delete('/{id}', response_class=Response, status_code=status.HTTP_204_NO_CONTENT)
def delete_link(
  id: int,
  service: LinkService = Depends(),
  user: DetailUserJwt = Depends(get_current_user)
):
  return service.delete_link(
    user_id=user.id,
    link_id=id
  )



