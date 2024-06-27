from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired, Email



class Technician(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    senha = StringField('Senha', validators=[DataRequired()])
    
    
