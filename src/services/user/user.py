from typing import List

from fastapi import (
	HTTPException, 
	status
)

from src.db.user import UserDb
from src.services.crud import CRUDService


class UserService(CRUDService):
	def get_all_users(self) -> List[UserDb]:
		users = self.get_all_elements(UserDb)
		return users

	def get_user_by_id(self, user_id: int) -> UserDb:
		user = self.get_element_by_id(UserDb, user_id)
		if not user:
			raise HTTPException(
				status_code=status.HTTP_404_NOT_FOUND,
				detail=f"user with id {user_id} not found"
			)
		return user

	def get_user_by_username(self, username: str):
		user = self.session.query(UserDb).filter(UserDb.username==username).first()
		if not user:
			return ""
		return user

	def check_user_is_owner(self, user, user_id):
		if not user.id == user_id:
			raise HTTPException(
				status_code=status.HTTP_403_FORBIDDEN,
				detail="you don't have access"
			)
		return user

	def delete_user(self, id: int, user_id):
		user = self.get_user_by_id(id)
		user = self.check_user_is_owner(user, user_id)
		self.delete(user)
		return ''

	




