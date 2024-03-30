from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators

#Formulario de Cadastro
class FormularioTarefa(FlaskForm):
    descricao = StringField('descricao',[validators.DataRequired(), validators.length(min=0, max=100)])
    cadastrar = SubmitField('Cadastrar')