from utils.db import db


class Boleto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    fecha_inicio = db.Column(db.DateTime)
    fecha_fin = db.Column(db.DateTime)
    numTotal_boletos = db.Column(db.Integer)

    def __init__(self, nombre, fecha_inicio, fecha_fin, numTotal_boletos):
        self.nombre = nombre
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.numTotal_boletos = numTotal_boletos
