from fastapi import APIRouter, Depends
from apps.authtoken.security import TokenAuthentication
from apps.authtoken.security import authenticate_credentials


products = APIRouter()

token_scheme = TokenAuthentication(tokenUrl='token')

@products.get('/products/', tags=['products'])
async def get_products(token : str = Depends(token_scheme)):
    token = await authenticate_credentials(token)
    if token:
        return {'id' : 1, 'product': 'bag'}