from sennder.extensions import db


class CRUDMixin(object):
    """
    CRUDS operations for any SQLAlchemy instance.
    """

    @classmethod
    def create(cls, **kwargs):
        instance = cls(**kwargs)
        return instance.save()

    @classmethod
    def get_or_create(cls, **kwargs):
        instance = cls(**kwargs)
        return instance.save(merge=True)

    def update(self, commit=True, **kwargs):
        for attr, value in kwargs.items():
            setattr(self, attr, value)
        return commit and self.save() or self

    def save(self, commit=True, merge=False):
        if merge:
            return db.session.merge(self)
        db.session.add(self)
        if commit:
            db.session.commit()
        return self

    def delete(self, commit=True):
        db.session.delete(self)
        return commit and db.session.commit()


class Model(CRUDMixin, db.Model):
    """
    Base model with CRUD operations.
    """

    __abstract__ = True
