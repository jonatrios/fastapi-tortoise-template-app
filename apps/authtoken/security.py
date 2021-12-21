from typing import Dict, Optional
from fastapi.exceptions import HTTPException
from fastapi.requests import Request
from fastapi.security import OAuth2
from fastapi.security.utils import get_authorization_scheme_param
from starlette.status import HTTP_401_UNAUTHORIZED
from fastapi.openapi.models import OAuthFlow as OAuthFlowsModel

from apps.authtoken.models import Token
from .serializers import UserAuthenticateSerializer
from apps.user.models import UserModel
from tortoise.exceptions import DoesNotExist


class TokenAuthentication(OAuth2):
    def __init__(
        self,
        tokenUrl: str,
        scheme_name: Optional[str] = None,
        scopes: Optional[Dict[str, str]] = None,
        description: Optional[str] = None,
        auto_error: bool = True,
    ):
        if not scopes:
            scopes = {}
        flows = OAuthFlowsModel(password={"tokenUrl": tokenUrl, "scopes": scopes})
        super().__init__(
            flows=flows,
            scheme_name=scheme_name,
            description=description,
            auto_error=auto_error,
        )
    async def __call__(self, request: Request) -> Optional[str]:
        authorization: str = request.headers.get("Authorization")
        scheme, param = get_authorization_scheme_param(authorization)
        if not authorization or scheme.lower() != "token":
            if self.auto_error:
                raise HTTPException(
                    status_code=HTTP_401_UNAUTHORIZED,
                    detail="Not authenticated",
                    headers={"WWW-Authenticate": "Token"},
                )
            else:
                return None
        return param


async def authenticate_user(user : UserAuthenticateSerializer):
    try: 
        user_model = await UserModel.get(username=user.username)
    except DoesNotExist:
        return False
    if not user_model:
        return False
    if not user.validate_password(user_model.password):
        return False
    return user_model

async def authenticate_credentials(key:str):
    try:
        token = await Token.filter(key=key).prefetch_related('user')
        if token:
            return True
        raise HTTPException(status_code=HTTP_401_UNAUTHORIZED,
                    detail="invalid Credentials")
    except DoesNotExist:
        raise HTTPException(status_code=HTTP_401_UNAUTHORIZED,
                    detail="invalid Credentials")