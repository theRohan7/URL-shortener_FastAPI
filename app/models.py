from sqlalchemy import Column, String, Integer, DateTime
from app.database import Base

class Url(Base):
    __tablename__ = 'urls'

    id = Column(Integer, primary_key=True,index=True)
    original_url = Column(String, nullable=False)
    short_url = Column(String, nullable=False, unique=True, index=True)
