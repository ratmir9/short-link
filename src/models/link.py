from datetime import datetime

from pydantic import (
  BaseModel, 
  HttpUrl
)


class BaseLink(BaseModel):
  origin_link: HttpUrl
  
  class Config:
    orm_mode = True


class CreateLink(BaseLink):
  short_link: str
  code: str
  owner_id: int


class DetailLink(BaseLink):
  id: int
  short_link: str
  click_counter: int
  created_at: datetime

