from typing import List
from fastapi import (
  HTTPException, 
  status
)
from pydantic import HttpUrl

from src.db.link import Link
from src.services.link.create_short_link import CreateShortLinkService
from src.services.crud import CRUDService
from src.models.link import CreateLink


class LinkService(CRUDService, CreateShortLinkService):
  def get_all_links(self) -> List[Link]:
    links = self.get_all_elements(Link)
    return links 

  def get_all_links_user(self, user_id) -> List[Link]:
    links = (
      self.session
      .query(Link)
      .filter(Link.owner_id==user_id)
      .all()
    )
    return links

  def get_link_by_id(self, link_id: int) -> Link:
    link =  self.get_element_by_id(Link, link_id)
    if not link:
      raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail='not link'
      )
    return link

  def check_user_is_owner(self, link: int, user_id: int) -> Link :
    if not link.owner_id==user_id:
      raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="you don't have access"
      )
    return link

  def get_link_by_code(self, code: str) -> Link:
    link = (
      self.session
      .query(Link)
      .filter_by(code=code)
      .first()
    )
    if not link:
      raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="link not found"
      )
    return link

  def detail_link(self, link_id: int, user_id: int) -> Link:
    link = self.get_link_by_id(link_id)
    return self.check_user_is_owner(link, user_id)

  def increment_counter(self, link: Link) -> Link:
    link.click_counter += 1
    return link

  def redirect_code(self, code: str) -> str:
    link = self.get_link_by_code(code)
    if link:
      self.increment_counter(link)
      self.session.commit()
      return link.origin_link

  def create_link(self, user_id, origin_link: HttpUrl) -> Link:
    code, short_link = self._create_short_link()    
    create_link = CreateLink(
      origin_link=origin_link,
      short_link=short_link,
      code=code,
      owner_id=user_id
    )
    link = self.create(Link, create_link)
    return link

  def delete_link(self, link_id: int, user_id: int):
    link = self.get_link_by_id(link_id)
    link = self.check_user_is_owner(link, user_id)
    self.delete(link)
    return ''


  
