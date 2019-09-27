import os
import datetime
import jwt

from sqlalchemy import (Column, String, String, ForeignKey, Integer, DECIMAL)
from sqlalchemy.orm import relationship
from sqlalchemy.schema import Sequence

from helpers.database import Base
from utilities.utility import Utility

secret = os.getenv('SECRET_KEY')

class Trip(Base, Utility):
    __tablename__ = 'trips'
    id = Column(Integer, Sequence('users_id_seq', start=1), primary_key=True)  # noqa
    host_id = Column(Integer, ForeignKey('users.id', ondelete="CASCADE"))
    estimated_time = Column(String, nullable=False)
    distance = Column(String, nullable=False)
    destination_address =  Column(String, nullable=False)
    destination_longitude = Column(DECIMAL(10,2), nullable=False)
    destination_latitude = Column(DECIMAL(10,2), nullable=False)
    host = relationship('User', uselist=False, foreign_keys=[host_id])
    status = Column(String, nullable=False, default='started')
    start_address = Column(String, nullable=False)
    start_longitude = Column(DECIMAL(10,2), nullable=False)
    start_latitude = Column(DECIMAL(10,2), nullable=False)
