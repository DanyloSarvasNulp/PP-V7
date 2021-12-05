from DataBase.models import User, Access, Auditorium


user1 = User(username="pusyBOY", email="customemail@gmail.com", phone="0935215742")
user2 = User(username="SLAVIC", email="slavemail@gmail.com", phone="0357315412")
user3 = User(username="Khodack", email="nikeriss@gmail.com", phone="0163715556")

auditorium1 = Auditorium(is_free=True)
auditorium2 = Auditorium(is_free=True)

access1 = Access(auditorium_id=1, user_id=1)
access2 = Access(auditorium_id=2, user_id=2)

with Session() as session:
    session.add(user1)
    session.add(user2)
    session.add(user3)
    session.commit()

    session.add(auditorium1)
    session.add(auditorium2)
    session.commit()

    session.add(access1)
    session.add(access2)
    session.commit()


print(session.query(User).all()[0])

