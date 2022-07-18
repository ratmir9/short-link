from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from src.models.user import DetailUserJwt
from .auth import AuthService


oauth_schema = OAuth2PasswordBearer(tokenUrl='/api/v1/auth/login')

def get_current_user(
	service: AuthService = Depends(),
	token: str = Depends(oauth_schema)
) -> DetailUserJwt:
	return service.validate_token(token)
