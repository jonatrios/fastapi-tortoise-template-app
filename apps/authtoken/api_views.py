from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from starlette import status
from starlette.responses import JSONResponse
from .serializers import UserAuthenticateSerializer
from .security import authenticate_user
from .models import Token

authtoken = APIRouter()

@authtoken.post('/obtain-token/', tags=['token_obtain'])
async def obtain_token(credentials: UserAuthenticateSerializer):
    if credentials.username == None or credentials.password == None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Invalid credentials",)
    user = await authenticate_user(credentials)
    if user:
        token = await Token.get_or_create(user=user)
        print(token[0].key)
        return JSONResponse(content={'token': token[0].key})
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Invalid credentials")

