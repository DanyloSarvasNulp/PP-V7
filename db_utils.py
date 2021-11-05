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


def get_entry_by_username(model_class, username, **kwargs):
    session = Session()
    return session.query(model_class).filter_by(username=username, **kwargs).first()
