from ninja import Router

from .news import router as news_router
from .about import router as about_router
from .categories import router as categories_router
from .history import router as history_router
from .products import router as products_router
from .vacancies import router as vacancies_router


router = Router()

router.add_router('/news/', news_router)
router.add_router('/about/', about_router)
router.add_router('/categories/', categories_router)
router.add_router('/history/', history_router)
router.add_router('/products/', products_router)
router.add_router('/vacancies/', vacancies_router)
