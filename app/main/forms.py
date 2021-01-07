from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired

class AddLibrary(FlaskForm):
    description = StringField('Nome da Biblioteca', validators=[DataRequired()])
    adress = StringField('Endereço da Biblioteca', validators=[DataRequired()])
    cadastrar = SubmitField('Cadastrar')


class AddUser(FlaskForm):
    name = StringField('Nome do Associado', validators=[DataRequired()])
    sex = StringField('Sexo do associado', validators=[DataRequired()])
    cadastrar = SubmitField('Cadastrar')

class AddBook(FlaskForm):
    isbn = IntegerField('ISBN do Livro (Somente números)', validators=[DataRequired()])
    title = StringField('Título do livro', validators=[DataRequired()])
    name = StringField('Nome do Autor', validators=[DataRequired()])
    description = StringField('Assunto do livro', validators=[DataRequired()])
    belongs = IntegerField('Código da biblioteca em que o livro se encontra', validators=[DataRequired()])
    cadastrar = SubmitField('Cadastrar novo Livro')

