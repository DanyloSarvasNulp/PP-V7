from models import Session, user, access, querry, auditorium


user1 = user(username="pusyBOY",email="customemail@gmail.com", phone="0935215742")
user2 = user(username="SLAVIC",email="slavemail@gmail.com", phone="0357315412")
user3 = user(username="Khodack",email="nikeriss@gmail.com", phone="0163715556")

auditorium1 = auditorium(is_free=True)
auditorium2 = auditorium(is_free=True)

querry1 = querry(place=4)
querry2 = querry(place=10)

access1 = access(auditorium_id=1, user_id=1, querry_id=1)
access2 = access(auditorium_id=2, user_id=2, querry_id=2)

with Session() as session:
    # session.add(user1)
    # session.add(user2)
    # session.add(user3)
    # session.add(auditorium1)
    # session.add(auditorium2)
    # session.add(querry1)
    # session.add(querry2)
    session.add(access1)
    session.add(access2)
    session.commit()


print(session.query(user).all()[0])

