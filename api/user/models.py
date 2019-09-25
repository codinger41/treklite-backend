import os
import datetime
import jwt

from sqlalchemy import (Column, String, Integer)
from sqlalchemy.orm import relationship
from sqlalchemy.schema import Sequence

from helpers.database import Base
from utilities.utility import Utility

secret = os.getenv('SECRET_KEY')

class User(Base, Utility):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('users_id_seq', start=1), primary_key=True)  # noqa
    fullname = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=True)
    profile_photo = Column(String, nullable=True)
    phone = Column(String, nullable=True)
    created_at = Column(String, default=datetime.datetime.now)
    updated_at = Column(String, default=datetime.datetime.now)

    def generate_token(self):
        token = jwt.encode(
            {'id': str(self.id)},
            secret,
            algorithm='HS256'
        )

        return token.decode('utf-8')

    def decode_token(self, token):
        payload = jwt.decode(
            token,
            secret,
            algorithms=['HS256']
        )

        return payload
