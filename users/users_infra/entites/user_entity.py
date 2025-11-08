import datetime

from sqlalchemy import Column, String, DateTime, BigInteger

from config.database import Base


class UserEntity(Base):

    __tablename__ = 'users'

    user_id = Column(BigInteger, primary_key=True, autoincrement=False)
    name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    encrypted_password = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
