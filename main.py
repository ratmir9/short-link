import  uvicorn 

from src import app
from src.core.settings import SERVER_HOST, SERVER_PORT


if __name__ == '__main__':
  uvicorn.run(
    "main:app",
    host=SERVER_HOST,
    port=SERVER_PORT,
    reload=True  
  ) 
