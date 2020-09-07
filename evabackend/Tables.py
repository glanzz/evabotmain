from sqlalchemy import Column, String, Integer, Float, Table, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

#user_info table
class UserInfo(Base):
    __tablename__ = "user_info"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(255), nullable=False)
    school_id = Column(String(255))
    family_score = Column(Float, default=0)
    friends_score = Column(Float, default=0)
    teachers_score = Column(Float, default=0)
        

#potential_reasons table
class PotentialReasons(Base):
    __tablename__="potential_reasons"
    id=Column(Integer, primary_key=True)
    question=Column(String(1000), nullable=False)
    answer=Column(String(1000), nullable=False)
    user_id = Column(Integer, ForeignKey('user_info.id'))