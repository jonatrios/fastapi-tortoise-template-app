from datetime import datetime
from typing import List
from fastapi import APIRouter
from .serializers import UserSerializer, UserSerializerIn
from .models import UserModel


user = APIRouter()


@user.get('/user/',response_model=List[UserSerializer])
async def get_users():
    return await UserSerializer.from_queryset(UserModel.all())

@user.post('/user/', response_model=UserSerializer)
async def create_user(user: UserSerializerIn):
    user.parse_date(user.date_of_birth)
    user_db = await UserModel.create(**user.dict(exclude_unset=True))
    return await UserSerializer.from_tortoise_orm(user_db)

@user.put('/user/{user_id}', response_model=UserSerializer)
async def update_user(user_id:int, user:UserSerializerIn):
    user.parse_date(user.date_of_birth)
    print(user)
    user = await UserModel.filter(id=user_id).update(**user.dict(exclude_unset=True))
    print(user)
    return await UserSerializer.from_queryset_single(UserModel.get(id=user))

