from models import Session


def create_entry(model_class, commit=True, **kwargs):  # POST entity
    session = Session()
    entry = model_class(**kwargs)
    session.add(entry)
    if commit:
        session.commit()
    return entry


def get_entry_by_id(model_class, id):  # GET all entries
    session = Session()
    return session.query(model_class).filter_by(id=id).first()


def get_entry_by_username(model_class, username):  # GET user by username
    session = Session()
    return session.query(model_class).filter_by(username=username).first()


def update_entry_by_id(model_class, id, commit=True, **kwargs):  # PUT entity by id
    session = Session()
    model = session.query(model_class).filter_by(id=id).first()
    for key, value in kwargs.items():
        setattr(model, key, value)
    if commit:
        session.commit()
    return model


def delete_entry_by_id(model_class, id, commit=True):  # DELETE entity by id
    session = Session()
    model = session.query(model_class).filter_by(id=id).first()
    session.delete(model)
    if commit:
        session.commit()
    return model


def get_entry_by_ids(model_class, user_id, auditorium_id):  # GET access by user and auditorium ids
    session = Session()
    return session.query(model_class).filter_by(user_id=user_id, auditorium_id=auditorium_id).first()


def delete_entry_by_ids(model_class, user_id, auditorium_id, commit=True):  # DELETE access by user and auditorium ids
    session = Session()
    model = session.query(model_class).filter_by(user_id=user_id, auditorium_id=auditorium_id).first()
    session.delete(model)
    if commit:
        session.commit()
    return model
