import datetime
from tortoise.models import Model
from tortoise import fields


class UserModel(Model):
    username = fields.CharField(unique=True, null=False, blank=False, max_length=50)
    name = fields.CharField(max_length=255)
    last_name = fields.CharField(max_length=255)
    is_active = fields.BooleanField(default=True)
    date_of_birth = fields.DateField(null=True)
    created_at = fields.DateField(default=datetime.datetime.now)

    def __str__(self) -> str:
        return self.username

    class PydanticMeta:
        pass

    class Meta:
        table = "user"



class Location(Model):
    location_name = fields.CharField(max_length=200)
    code = fields.CharField(max_length=2)

    def __str__(self) -> str:
        return self.location_name

    class Meta:
        table = 'location'