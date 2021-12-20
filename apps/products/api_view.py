from fastapi import APIRouter

products = APIRouter()

@products.get('/products/')
async def get_products():
    return {'id' : 1}