import uuid

from src.core.settings import (
  SERVER_HOST,
  SERVER_PORT,
  PREFIX_URL_LINK
)


class CreateShortLinkService:
  def _generate_short_code(self)-> str:
    return str(uuid.uuid4()).split('-')[0]

  def _create_short_link(self):
    code = self._generate_short_code()
    short_link = f'http://{SERVER_HOST}:{SERVER_PORT}{PREFIX_URL_LINK}/{code}'
    return code, short_link