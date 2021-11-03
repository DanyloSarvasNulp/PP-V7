from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import Column, Integer, ForeignKey, VARCHAR, DateTime, Boolean

engine = create_engine('mysql+pymysql://root:22121356@127.0.0.1/swagger_booking')
engine.connect()

SessionFactory = sessionmaker(bind=engine)

Session = scoped_session(SessionFactory)

BaseModel = declarative_base()


class user(BaseModel):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    username = Column(VARCHAR(45))
    firstName = Column(VARCHAR(45))
    lastName = Column(VARCHAR(45))
    email = Column(VARCHAR(45))
    password = Column(VARCHAR(45))
    phone = Column(VARCHAR(15))
    userStatus = Column(Boolean)

    def __str__(self):
        return f"User ID    : {self.id}\n" \
               f"Username      : {self.username}\n" \
               f"Email      : {self.email}\n" \
               f"phone      : {self.phone}\n"

class auditorium(BaseModel):
    __tablename__ = "auditorium"

    id = Column(Integer, primary_key=True)
    is_free = Column(Boolean)


class access(BaseModel):
    __tablename__ = "access"
    id = Column(Integer, primary_key=True)
    auditorium_id = Column(Integer, ForeignKey(auditorium.id))
    user_id = Column(Integer, ForeignKey(user.id))
    start = Column(DateTime)
    end = Column(DateTime)


BaseModel.metadata.create_all(engine)


