from ninja import Router

from .about import router as about_router
from .history import router as history_router
from .homepage import router as homepage_router
from .news import router as news_router
from .products import router as products_router
from .user_requests import router as user_requests_router
from .vacancies import router as vacancies_router

router = Router()

router.add_router("/news/", news_router)
router.add_router("/about/", about_router)
router.add_router("/history/", history_router)
router.add_router("/products/", products_router)
router.add_router("/vacancies/", vacancies_router)
router.add_router("/homepage/", homepage_router)
router.add_router("/user_requests/", user_requests_router)
