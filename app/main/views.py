from flask import render_template, session, redirect, url_for, current_app
from . import main
from .forms import AddLibrary, AddBook
from .. import db
from  ..models import Library, Book, Author,Subject


@main.route('/')
def index():
    return render_template('index.html')

@main.route('/sucess')
def sucess():
    return render_template('sucess.html')


@main.route('/register_lib', methods=['GET','POST'])
def add_library():
    form_lib = AddLibrary()
    if form_lib.validate_on_submit():
        library = Library.query.filter_by(description=form_lib.description.data).first()
        if library is None:
            library = Library(description=form_lib.description.data, adress=form_lib.adress.data)
            db.session.add(library)
            db.session.commit()
        return redirect(url_for('.sucess'))
    return render_template('register_lib.html', form_lib=form_lib)

@main.route('/register_book', methods=['GET', 'POST'])
def add_book():
    form_book = AddBook()
    if form_book.validate_on_submit():
        book = Book.query.filter_by(title=form_book.title.data).first()
        author = Author.query.filter_by(name=form_book.name.data).first()
        subject = Subject.query.filter_by(description=form_book.description.data).first()
        if book is None:
            book = Book(isbn=form_book.isbn.data ,title=form_book.title.data, belongs=form_book.belongs.data)
            db.session.add(book)
            db.session.commit()
            if author is None:
                author = Author(name=form_book.name.data)
                db.session.add(author)
                db.session.commit()
                if subject is None:
                    subject = Subject(description=form_book.description.data)
                    db.session.add(subject)
                    db.session.commit()
                return redirect(url_for('.sucess'))
            return redirect(url_for('.sucess'))
        return redirect(url_for('.sucess'))
    return render_template('register_book.html', form_book=form_book)
