from flask_wtf import FlaskForm
from wtforms.fields.html5 import DecimalField, IntegerField
from wtforms import StringField, validators
from wtforms_components import read_only


class ProdutoForm(FlaskForm):
    id = IntegerField(label='Código', id='prod_id')

    nome = StringField(label='Nome', id='nome',
        validators=[validators.InputRequired('O nome é obrigatório.')])

    vr_venda = DecimalField(label='Valor de venda', id='vr_venda', default=0.00,
        validators=[validators.InputRequired('O valor de venda é obrigatório.')])

    vr_custo = DecimalField(label='Valor de custo', id='vr_custo', default=0.00,
        validators=[validators.InputRequired('O valor de custo é obrigatório.')])

    def __init__(self, *args, **kwargs):
        super(ProdutoForm, self).__init__(*args, **kwargs)
        read_only(self.id)
