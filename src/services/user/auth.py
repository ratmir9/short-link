from datetime import (
	datetime, 
	timedelta
)
from fastapi import (
	HTTPException, 
	status
) 
from passlib.hash import bcrypt
from jose import (
	JWTError, 
	jwt
)
from pydantic import ValidationError
from sqlalchemy.exc import IntegrityError

from src.core.settings import (
	JWT_SECRET_KEY,
	JWT_ALGORITHM,
	jwt_expiration
)
from src.models.user import (
	DetailUserJwt,
 	CreateUser,
 	CreateUserDb,
 	DetailUser
 )
from src.models.auth import Token
from src.db.user import UserDb
from src.services.user.user import UserService 


class AuthService(UserService):
	def verify_password(self, hash_password: str, plain_password: str) -> bool:
		return bcrypt.verify(plain_password, hash_password)

	def hash_password(self, password: str)-> str:
		return bcrypt.hash(password)

	def validate_token(self, token: str)-> DetailUserJwt:
		exception = HTTPException(
			status_code=status.HTTP_401_UNAUTHORIZED,
			detail='Could not validate token',
			headers={
				'BAD-Authenticate': 'Bearer'
			},
		)
		try:
			payload = jwt.decode(
				token,
				JWT_SECRET_KEY,
				algorithms=[JWT_ALGORITHM],
			)
		except JWTError:
			raise exception from None		
		user_data = payload.get('user')
		user_data = self.get_user_by_id(user_id=user_data['id'])
		user_data = DetailUserJwt.from_orm(user_data)
		print(user_data)
		try:
			user = DetailUserJwt.parse_obj(user_data)
		except ValidationError:
			raise exception from None
		return user

	def create_token(self, user: dict) -> Token:		
		current_datetime = datetime.utcnow()
		payload = {
			'exp': current_datetime + timedelta(seconds=jwt_expiration),
			'user': {
				'id': user['id'],
				'username': user['username'],
				'email': user['email'], 
			}
		}
		token = jwt.encode(
			payload,
			JWT_SECRET_KEY,
			algorithm=JWT_ALGORITHM
		)
		return Token(access_token=token)

	def register_new_user(self, user_data: CreateUser) -> DetailUser:
		new_user = CreateUserDb(
			username=user_data.username,
			email=user_data.email,
			password_hush=self.hash_password(user_data.password)
		)
		try: 
			result = self.create(UserDb, new_user)
		except IntegrityError as err:
			self.session.rollback()
			raise HTTPException(
				status_code=status.HTTP_400_BAD_REQUEST,
				detail=f'user such exists'
			)
		user = DetailUser.from_orm(result)
		return user
	
	def autenticate_user(self, username: str, password: str) -> Token:
		exception = HTTPException(
			status_code=status.HTTP_401_UNAUTHORIZED,
			detail='Interract username or password',
			headers={
				'BAD-Authenticate': 'Bearer'
			},
		)
		user = self.get_user_by_username(username)
		if not user:
			raise exception
		if not self.verify_password(user.password_hush, password):
			raise exception
		return user

	def clean_user_data(self, user):
		user_data = {
			'id': user.id,
			'username': user.username,
			'email': user.email
		}
		return user_data
		
	def login(self, username: str, password: str):
		user = self.autenticate_user(username, password)
		user_data = self.clean_user_data(user)
		return self.create_token(user_data)
	


	

