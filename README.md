# Сервис по сокращению ссылок


## Инструкция по установке и запуску проекта.

1. **Клонируйте репозитории с github.**

2. **Перейдмте в директорию с проектом.**
```
cd short-link/
```
### Запуск проекта без использования Docker.

1. **Создайте виртуальное окружение.**
```
python3 -m venv venv
```
2. **Активируйте виртуальное окружение.**
```
source venv/bin/activate
```
3. **Установите зависимости.**
```
pip install -r requirements.txt
```
4. **Создайте файл конфигурации (например `env.sh`).**
```
touch env.sh
```
5. **Создайте БД PostgreSQL.**

6. **Заполните файл конфигурации.**
```
export SERVER_HOST='localhost'
export SERVER_PORT=5000

# DATABASE ENV
export DB_USER='' # имя пользователя бд 
export DB_PASS='123QWE' # пароль от бд
export DB_HOST='localhost' 
export DB_NAME='link' # название бд

# JWT Authenticate
export JWT_SECRET_KEY = '12345-QWERT' ваш секретный ключ  
export JWT_ALGORITHM = 'HS256' # алгоритм шифрования
```
7. **Активируйте файл конфигурации.**
```
source env.sh
```
8. **Выполните комвнду для применения миграции.**
```
alembic upgrade head
```
9. **Запустите приложение.**
```
python main.py
```
### Запуск проекта с помощью Docker.
1. **Создайте файлы `.env` и `.env.db` для конфигурирования проекта.**
```
touch .env
touch .env.db
```
2. **Откройте файл `.env` и заполните следующими данными.**
```
# server env
SERVER_HOST=0.0.0.0
SERVER_PORT=8000

# env db
DB_USER=fast
DB_PASSWORD=1234QWE 
DB_NAME=short_link
DB_HOST=db
DB_PORT=5432

# env jwt 
JWT_SECRET_KEY=12345-QWERT
JWT_ALGORITHM=HS256

```
3. **Откройте файл `.env.db` и заполните следущими данными.**
```
POSTGRES_USER=fast
POSTGRES_PASSWORD=1234QWE
POSTGRES_DB=short_link
```
**Значение параметров для БД в файлах `.env` и `.env.db` должны совпадать.**

4. **Выполните следующую команду для запуска проекта.**
```
sudo docker-compose up -d
```
5. **Выполните следующую команду для применения миграции.**
```
sudo docker exec -it fast_app alembic upgrade head
```



