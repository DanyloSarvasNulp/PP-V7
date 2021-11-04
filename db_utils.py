
def create_entry(model_class, **kwargs):
    return model_class(**kwargs)


def get_entry_by_username(model_class, username):
    return model_class.query.filter_by(username=username).first()