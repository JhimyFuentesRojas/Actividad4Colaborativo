from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class FormAgregarTareas (FlaskForm):
    titulo =  StringField('Titulo', validators=[DataRequired()])
    descripcion = TextAreaField('Descripción')
    enviar  = SubmitField('Enviar')