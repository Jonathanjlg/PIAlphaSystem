from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired

class EquipamentoForm(FlaskForm):
    marca_id = SelectField('Marca', validators=[DataRequired()], coerce=int)
    quantidade = IntegerField('Quantidade', validators=[DataRequired()])
    acessorios = StringField('Acessórios', validators=[DataRequired()])
    observacoes = TextAreaField('Observações',validators=[DataRequired()])
    submit = SubmitField('Salvar')
