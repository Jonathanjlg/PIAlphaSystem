from app import db

class Equipamento(db.Model):
    __tablename__ = "equipamento"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    quantidade = db.Column(db.Integer)
    acessorios = db.Column(db.String(200))
    marca_id = db.Column(db.Integer, db.ForeignKey('marca.id'), nullable=False)

    marca = db.relationship('Marca', back_populates='equipamentos')