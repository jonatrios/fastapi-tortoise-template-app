import os
import binascii
from typing import Iterable, Optional
from tortoise import fields, models
from tortoise.backends.base.client import BaseDBAsyncClient

class Token(models.Model):
    ''' model to generate the Token'''
    key = fields.CharField(max_length=40)
    user = fields.OneToOneField('models.UserModel', on_delete=fields.CASCADE)
    created = fields.DatetimeField(auto_now_add=True)

    @classmethod
    async def generate_key(cls):
        return binascii.hexlify(os.urandom(20)).decode()

    async def save(self, using_db: Optional[BaseDBAsyncClient] = None, update_fields: Optional[Iterable[str]] = None, force_create: bool = False, force_update: bool = False) -> None:
        if not self.key:
            self.key = await self.generate_key()
        return await super().save(using_db=using_db, update_fields=update_fields, force_create=force_create, force_update=force_update)