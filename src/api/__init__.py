from fastapi import APIRouter

from src.api.link import router as link_router
from src.api.user import router as user_router
from src.api.auth import router as auth_router
from src.api.redirect_link import router as redirect_link


router = APIRouter()
router.include_router(link_router, prefix='/api/v1/links', tags=['links'])
router.include_router(user_router, prefix='/api/v1/users', tags=['users'])
router.include_router(auth_router, prefix='/api/v1/auth', tags=['auth'])
router.include_router(redirect_link, prefix='')





