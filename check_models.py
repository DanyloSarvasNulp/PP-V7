from models import Session, user, access, querry, auditorium

session = Session()

user1 = user(username="pusyBOY",email="customemail@gmail.com", phone="0935215742")

auditorium1 = auditorium(is_free=True)

querry1 = querry(place=4)

access1 = access(auditorium_id=1, user_id=1, querry_id=1)

session.add(user1)
# session.add(auditorium1)
# session.add(querry1)
# session.add(access1)
session.commit()


# print(session.query(user).all()[0])


session.close()
