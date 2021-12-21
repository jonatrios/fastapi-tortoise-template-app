from typing import List
from fastapi import APIRouter, status
from starlette.responses import JSONResponse
from .serializers import UserSerializer, UserSerializerIn, UserDeleteResponse
from .models import UserModel
from passlib.hash import pbkdf2_sha256


user = APIRouter()


@user.get('/user/',response_model=List[UserSerializer], tags=['user'])
async def get_users():
    return await UserSerializer.from_queryset(UserModel.all())

@user.post('/user/', response_model=UserSerializer, tags=['user'])
async def create_user(user: UserSerializerIn):
    user.parse_date(user.date_of_birth)
    user.password = pbkdf2_sha256.hash(user.password)
    user_db = await UserModel.create(**user.dict(exclude_unset=True))
    return await UserSerializer.from_tortoise_orm(user_db)


@user.get('/user/{user_id}', response_model=UserSerializer, tags=['user'])
async def get_user_detail(user_id:int):
    user = await UserModel.filter(id=user_id).first()
    if user:
        return await UserSerializer.from_queryset_single(user.get(id=user_id))
    return JSONResponse(content={'error': f'user id {user_id} does not exist'}, status_code=status.HTTP_400_BAD_REQUEST)

@user.put('/user/{user_id}', response_model=UserSerializer, tags=['user'])
async def update_user(user_id:int, user:UserSerializerIn):
    user.parse_date(user.date_of_birth)
    print(user)
    user = await UserModel.filter(id=user_id).update(**user.dict(exclude_unset=True))
    print(user)
    return await UserSerializer.from_queryset_single(UserModel.get(id=user))


@user.delete('/user/{user_id}', response_model=UserDeleteResponse, tags=['user'])
async def delete_user(user_id:int):
    user = await UserModel.filter(id=user_id).first()
    if user:
        await user.delete()
        return JSONResponse(content={'msg': f'user id {user_id} deleted succesfuly'}, status_code=status.HTTP_200_OK)
    return JSONResponse(content={'error': f'user id {user_id} does not exist'}, status_code=status.HTTP_400_BAD_REQUEST)