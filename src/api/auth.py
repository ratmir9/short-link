from fastapi import (
  APIRouter, 
  Depends,
  status
)
from fastapi.security import OAuth2PasswordRequestForm
from src.models.user import CreateUser
from src.services.user.auth import AuthService


router = APIRouter()

@router.post('/register', status_code=status.HTTP_201_CREATED)
def register(
  user_data: CreateUser,
  service: AuthService = Depends()
):
  return service.register_new_user(user_data)


@router.post('/login')
def login(
  form_data: OAuth2PasswordRequestForm = Depends(),
  service: AuthService = Depends()
):
  return service.login(
    username=form_data.username,
    password=form_data.password
  )







