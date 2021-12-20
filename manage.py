from fastapi import FastAPI
from app_factory import init

app = FastAPI()

init(app)



