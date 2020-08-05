from sennder.database import db, Model

movies = db.Table(
    'movies',
    db.Model.metadata,
    db.Column(
        'film_id',
        db.String(36),
        db.ForeignKey('films.id'),
        primary_key=True
    ),
    db.Column(
        'people_id',
        db.String(36),
        db.ForeignKey('peoples.id'),
        primary_key=True
    ),
)


class Film(Model):
    '''
    Film model.
    '''

    __tablename__ = 'films'

    id = db.Column(db.String(36), primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)

    def __repr__(self):
        return self.title


class People(Model):
    '''
    People model.
    '''

    __tablename__ = 'peoples'

    id = db.Column(db.String(36), primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    films = db.relationship(
        'Film',
        secondary=movies,
        lazy='dynamic',
        backref=db.backref('peoples', lazy='dynamic')
    )

    def __repr__(self):
        return self.name
