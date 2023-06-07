from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class ApiCall(Base):
    __tablename__ = 'api_calls'

    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, nullable=False)
    endpoint = Column(String, nullable=False)
    params = Column(JSON, nullable=True)
    result = Column(String, nullable=False)
