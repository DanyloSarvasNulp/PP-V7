from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import Column, Integer, ForeignKey, VARCHAR, DateTime, Boolean

engine = create_engine('mysql+pymysql://root:password@127.0.0.1/pp')
engine.connect()

SessionFactory = sessionmaker(bind=engine)

Session = scoped_session(SessionFactory)

BaseModel = declarative_base()
BaseModel.query = Session.query_property()


class User(BaseModel):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    username = Column(VARCHAR(45), unique=True)
    first_name = Column(VARCHAR(45))
    last_name = Column(VARCHAR(45))
    email = Column(VARCHAR(45))
    password = Column(VARCHAR(100))
    phone = Column(VARCHAR(15))
    user_status = Column(Boolean)

    def __str__(self):
        return f"User ID    : {self.id}\n" \
               f"Username      : {self.username}\n" \
               f"Email      : {self.email}\n" \
               f"Phone      : {self.phone}\n"

    def __init__(self, username, first_name=None, last_name=None, email=None, password=None, phone=None, user_status=False):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.phone = phone
        self.user_status = user_status


class Auditorium(BaseModel):
    __tablename__ = "auditorium"

    id = Column(Integer, primary_key=True)
    auditorium_num = Column(Integer, unique=True)
    max_people_count = Column(Integer)
    is_free = Column(Boolean)

    def __init__(self, auditorium_num=None, max_people_count=None, is_free=True):
        self.auditorium_num = auditorium_num
        self.max_people_count = max_people_count
        self.is_free = is_free


class Access(BaseModel):
    __tablename__ = "access"

    id = Column(Integer, primary_key=True)
    auditorium_id = Column(Integer, ForeignKey(Auditorium.id))
    user_id = Column(Integer, ForeignKey(User.id))
    start = Column(DateTime)
    end = Column(DateTime)

    def __init__(self, auditorium_id, user_id, start, end):
        self.auditorium_id = auditorium_id
        self.user_id = user_id
        self.start = start
        self.end = end


BaseModel.metadata.create_all(engine)
