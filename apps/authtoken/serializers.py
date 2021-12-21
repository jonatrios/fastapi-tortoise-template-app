from pydantic import BaseModel
from passlib.hash import pbkdf2_sha256


class UserAuthenticateSerializer(BaseModel):
	username : str
	password : str

	def validate_password(self, password):
		return pbkdf2_sha256.verify(self.password, password)


