from models import Session


def create_entry(model_class, commit=True, **kwargs):
    session = Session()
    entry = model_class(**kwargs)
    session.add(entry)
    if commit:
        session.commit()
    return entry


def get_entry_by_id(model_class, id, **kwargs):
    session = Session()
    return session.query(model_class).filter_by(id=id, **kwargs).first()


def get_entry_by_username(model_class, username, **kwargs):  # user-only
    session = Session()
    return session.query(model_class).filter_by(username=username, **kwargs).first()


def update_entry_by_id(model_class, id, commit=True, **kwargs):
    session = Session()
    model = session.query(model_class).filter_by(id=id).first()
    for key, value in kwargs.items():
        setattr(model, key, value)
    if commit:
        session.commit()
    return model


def delete_entry_by_id(model_class, id, commit=True):
    session = Session()
    model = session.query(model_class).filter_by(id=id).first()
    session.delete(model)
    if commit:
        session.commit()
    return model