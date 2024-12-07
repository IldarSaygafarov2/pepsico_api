from ninja import Router
from .routes import router as api_router


router = Router()

router.add_router('/v1/', api_router)
