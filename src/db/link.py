from datetime import datetime

import sqlalchemy as sa
from sqlalchemy.orm import relationship, backref 

from src.core.database_config import Base


class Link(Base):
  __tablename__ = 'links'

  id = sa.Column(sa.Integer, primary_key=True, unique=True)
  origin_link = sa.Column(sa.String)
  short_link = sa.Column(sa.String, unique=True)
  code = sa.Column(sa.String(10), unique=True)
  click_counter = sa.Column(sa.Integer, default=0)
  owner_id = sa.Column(sa.Integer, sa.ForeignKey('users.id'), nullable=False)
  created_at = sa.Column(sa.DateTime, default=datetime.utcnow)

  owner = relationship(
    "UserDb",
    backref=backref('links', cascade='all, delete-orphan')
  )


  