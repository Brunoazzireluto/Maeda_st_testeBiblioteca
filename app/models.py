from . import db


userlibs = db.Table('userlib',
    db.Column('code', db.Integer, db.ForeignKey('libraries.code')),
    db.Column('registration', db.Integer, db.ForeignKey('users.registration'))
    )

userloans = db.Table('loans',
    db.Column('isbn', db.Integer, db.ForeignKey('books.isbn')),
    db.Column('registration', db.Integer, db.ForeignKey('users.registration'))
    )

class Library(db.Model):
    __tablename__ = 'libraries'
    code = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(60), unique=True)
    adress = db.Column(db.String(60), unique=True)
    usuarios = db.relationship('User',secondary='userlib', backref=db.backref('user_id', lazy='dynamic'))
    books = db.relationship('Book', backref='book_code')

class User(db.Model):
    __tablename__ = 'users'
    registration = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(40))
    sex = db.Column(db.String(10))
    loans = db.relationship('Book', secondary='loans', backref=db.backref('book_loan', lazy='dynamic'))

author_book = db.Table('authorbook',
    db.Column('isbn', db.Integer, db.ForeignKey('books.isbn')),
    db.Column('code', db.Integer, db.ForeignKey('authors.code'))
    )

subject_book = db.Table('subjectbook',
    db.Column('isbn', db.Integer, db.ForeignKey('books.isbn')),
    db.Column('code', db.Integer, db.ForeignKey('subject.code'))
    )

class Book(db.Model):
    __tablename__ = 'books'
    isbn = db.Column(db.Integer, unique=True, primary_key=True)
    title = db.Column(db.String(60))
    belongs = db.Column(db.Integer, db.ForeignKey('libraries.code'))
    autores = db.relationship('Author',secondary='authorbook', backref=db.backref('author_id', lazy='dynamic'))
    assuntos = db.relationship('Subject', secondary='subjectbook',backref=db.backref('subject_id', lazy='dynamic'))

class Author(db.Model):
    __tablename__ = 'authors'
    code = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60))


class Subject(db.Model):
    __tlabename__ = 'subject'
    code = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(100))