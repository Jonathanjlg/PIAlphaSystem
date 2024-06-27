from app import db

class Orcamento(db.Model):
    __tablename__ = "orcamento"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    quantidade = db.Column(db.String(50))
    item = db.Column(db.String(50))
    valor_unit = db.Column(db.String(30))
    observacoes = db.Column(db.Text, nullable=False)

    fk_tecnico_id = db.Column(db.Integer, db.ForeignKey('tecnico.id'))
    fk_cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'))
    fk_servico_id = db.Column(db.Integer, db.ForeignKey('servico.id'))
    fk_equipamento_id = db.Column(db.Integer, db.ForeignKey('equipamento.id'))

    # Defina os relacionamentos com as outras tabelas aqui, se já estiverem definidas
    tecnico = db.relationship('Tecnico', backref='orcamentos')
    cliente = db.relationship('Cliente', backref='orcamentos')
    servico = db.relationship('Servico', backref='orcamentos')
    equipamento = db.relationship('Equipamento', backref='orcamentos')