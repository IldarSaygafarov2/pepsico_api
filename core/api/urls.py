from ninja import NinjaAPI
from .v1 import router as v1_router



api = NinjaAPI()


api.add_router('/api/', v1_router)
