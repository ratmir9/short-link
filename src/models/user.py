from datetime import datetime

from pydantic import (
	BaseModel, 
	EmailStr
)


class BaseUser(BaseModel):
	username: str
	email: EmailStr

	class Config:
		orm_mode = True

class DetailUser(BaseUser):
	id: int
	created_at: datetime


class DetailUserJwt(BaseUser):
	id: int
		

class CreateUser(BaseUser):
	password: str

class CreateUserDb(BaseUser):
	password_hush: str

