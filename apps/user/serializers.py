from datetime import datetime
from tortoise.contrib.pydantic import pydantic_model_creator
from pydantic import BaseModel
from .models import UserModel


UserSerializer = pydantic_model_creator(UserModel, name='UserSerializer')


class UserSerializerIn(BaseModel):
    username : str
    name : str
    last_name : str
    date_of_birth : str

    def parse_date(self, value):
        self.date_of_birth = datetime.strptime(value, '%d/%m/%Y').strftime('%Y-%m-%d')