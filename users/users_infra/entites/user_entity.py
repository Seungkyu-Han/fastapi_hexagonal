import datetime

from sqlalchemy import Column, Integer, String, DateTime

from config.database import Base


class UserEntity(Base):

    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    encrypted_password = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
