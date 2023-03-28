from .home import router as home_router
from .login import router as login_router
from .register import router as register_router
from fastapi import FastAPI

app = FastAPI()

app.include_router(home_router)
app.include_router(login_router)
app.include_router(register_router)
