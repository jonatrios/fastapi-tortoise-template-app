import datetime
from tortoise.models import Model
from tortoise import fields

class MesureUnitModel(Model):
    mesure_name = fields.CharField(unique=True, null=False, blank=False, max_length=50)
    description = fields.TextField()

    def __str__(self) -> str:
        return self.mesure_name


class CategoryModel(Model):
    category_name = fields.CharField(unique=True, null=False, blank=False, max_length=50)
    description = fields.TextField()

    def __str__(self) -> str:
        return self.category_name


class ProductModel(Model):
    product_name = fields.CharField(unique=True, null=False, blank=False, max_length=50)
    description = fields.CharField(max_length=255)
    created_at = fields.DateField(default=datetime.datetime.now)
    category = fields.ForeignKeyField('models.CategoryModel', on_delete=fields.CASCADE)
    mesure_unit = fields.ForeignKeyField('models.MesureUnitModel', on_delete=fields.CASCADE)


    def __str__(self) -> str:
        return self.product_name

    class PydanticMeta:
        pass

    class Meta:
        table = "products"