from fastapi import Depends
from sqlalchemy.orm import Session

from src.core.database_config import get_session


class CRUDService:
	def __init__(self, session: Session = Depends(get_session)):
		self.session = session

	def get_element_by_id(self, tablename, id):
		element = self.session.query(tablename).filter_by(id=id).first()
		return element

	def get_all_elements(self, db_name):
		data = self.session.query(db_name).all()
		return data

	def create(self, db_name, data):
		result = db_name(**data.dict())
		self.session.add(result)
		self.session.commit()
		return result

	def delete(self, obj):
		self.session.delete(obj)
		self.session.commit()
		return obj