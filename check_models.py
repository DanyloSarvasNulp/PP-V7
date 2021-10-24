from models import Session, user, access, querry, auditorium

session = Session()

user1 = user(id=1, username="pusyBOY", userStatus=True)

auditorium1 = auditorium(id=1, is_free=True)

querry1 = querry(id=1, place=1)

access1 = access(auditorium_id=1, user_id=1, querry_id=1)

session.add(user1)
session.add(auditorium1)
session.add(querry1)
session.add(access1)

print(session.query(user).all())

session.close()
