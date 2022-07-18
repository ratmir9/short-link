import os


SERVER_HOST = os.getenv('SERVER_HOST', 'localhost')
SERVER_PORT = int(os.getenv('SERVER_PORT', 5000))

DB_USER = os.getenv('DB_USER', 'root')
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_NAME = os.getenv('DB_NAME', '')
DB_PASS = os.getenv('DB_PASS', '')

PREFIX_URL_LINK = '/r'

DATABASE_URL = f'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:5432/{DB_NAME}'

JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'you-code')
JWT_ALGORITHM = os.getenv('JWT_ALGORITHM', 'HS256')

jwt_expiration: int = 5 * 60 * 60 
