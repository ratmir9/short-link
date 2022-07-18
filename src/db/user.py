from datetime import datetime

import sqlalchemy as sa

from src.core.database_config import Base


class UserDb(Base):
	__tablename__ = 'users'

	id = sa.Column(sa.Integer, primary_key=True, unique=True)
	username = sa.Column(sa.String(64), unique=True)
	email = sa.Column(sa.String, unique=True)
	password_hush = sa.Column(sa.String)
	created_at = sa.Column(sa.DateTime, default=datetime.utcnow)



