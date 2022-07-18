from fastapi import FastAPI

from src.api import router


app = FastAPI(
  title="Short link",
  description="Сервис по сокращению ссылок",
  version="1.0.0"
)

app.include_router(router)





