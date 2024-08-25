from fastapi import APIRouter
from usingNoSql.router import router as usingNoSql_router
from usingSql.router import router as usingSql_router

global_router = APIRouter(prefix="/api")

global_router.include_router(usingNoSql_router)
global_router.include_router(usingSql_router)