from app import db #SQLAlchemy - Migrate:Migrar Classe para Tabela

class Marca(db.Model):
    __tablename__ = "marca"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100), nullable=False)

    equipamentos = db.relationship('Equipamento', back_populates='marca')