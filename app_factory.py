from fastapi import FastAPI
from tortoise.contrib.starlette import register_tortoise
from settings import TortoiseSettings

tortoise_config = TortoiseSettings.generate()

migration_config = TortoiseSettings.migration_dict()

def init(app: FastAPI):
    """
    Init routers and etc.
    :return:
    """
    init_routers(app)
    init_db(app)


def init_db(app: FastAPI):
    """
    Init database models.
    :param app:
    :return:
    """
    register_tortoise(
        app,
        db_url=tortoise_config.db_url,
        generate_schemas=tortoise_config.generate_schemas,
        modules=tortoise_config.modules,
    )


def init_routers(app: FastAPI):
    """
    Initialize routers defined in `app.api`
    :param app:
    :return:
    """
    from apps.user.api_views import user
    from apps.products.api_view import products
    from apps.authtoken.api_views import authtoken

    routers = [user,products, authtoken]

    for router in routers:
        app.include_router(router)