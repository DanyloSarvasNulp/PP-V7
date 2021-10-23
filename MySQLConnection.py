
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import Column, Integer, ForeignKey, String, BigInteger, DateTime, BINARY, Boolean, func

engine = create_engine('mysql+pymysql://root:45627349350923@127.0.0.1/Swagger_booking')
engine.connect()


BaseModel = declarative_base()

class user(BaseModel):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    username = Column(String)
    firstName = Column(String)
    lastName = Column(String)
    email = Column(String)
    password = Column(String)
    phone = Column(String)
    userStatus = Column(Boolean)



class access(BaseModel):
    __tablename__ = "access"
    auditorium_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, primary_key=True)
    start = Column(DateTime)
    end = Column(DateTime)
    querry_id = Column(Integer, primary_key=True)

class querry(BaseModel):
    __tablename__ = "querry"

    id = Column(Integer, primary_key=True)
    place = Column(Integer)


class auditorium(BaseModel):
    __tablename__ = "auditorium"

    id = Column(Integer, primary_key=True)
    is_free = Column(Boolean)