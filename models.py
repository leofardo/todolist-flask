from app import db
from datetime import datetime

class Tarefas(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    descricao = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(30), nullable=False, default="Pendente")
    data_cadastro = db.Column(db.DateTime, nullable=False, default=datetime.now)

    def __repr__(self):
        return '<Name %r' % self.descricao