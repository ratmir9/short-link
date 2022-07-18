from typing import List

from fastapi import (
	APIRouter, 
	Depends,
	status
)
from fastapi.responses import Response
from src.models.user import (
	DetailUser, 
	DetailUserJwt
)
from src.services.user.user import UserService
from src.services.user.current_user import get_current_user


router = APIRouter()


@router.get('/', response_model=List[DetailUser])
def list_user(
	service: UserService = Depends(),
	user: DetailUserJwt = Depends(get_current_user)
):
	return service.get_all_users()


@router.get('/{id}', response_model=DetailUser)
def detail_user(
	id: int,
	service: UserService = Depends(),
	user: DetailUserJwt = Depends(get_current_user)
):
	return service.get_user_by_id(id)


@router.delete('/{id}', response_class=Response, status_code=status.HTTP_204_NO_CONTENT)
def delete_user(
	id: int,
	service: UserService = Depends(),
	user: DetailUserJwt = Depends(get_current_user)
):
	return service.delete_user(id, user_id=user.id)

	

