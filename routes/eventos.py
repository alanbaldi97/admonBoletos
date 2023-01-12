from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.evento import Evento
from utils.db import db

eventos = Blueprint("eventos", __name__)


@eventos.route('/')
def index():
    Evento = Evento.query.all()
    return render_template('index.html', eventos=eventos)


@eventos.route('/new', methods=['POST'])
def eventoNuevo():
    if request.method == 'POST':

        # Datos del form
        nombre = request.form['nombre']
        fecha_inicio = request.form['fecha_inicio']
        fecha_fin = request.form['fecha_fin']

        # Se crea un nuevo objeto del evento
        nuevo_evento = Evento(nombre, fecha_inicio, fecha_fin)

        # save the object into the database
        db.session.add(nuevo_evento)
        db.session.commit()

        flash('¡Evento agregado correctamente!')

        return redirect(url_for('eventos.index'))


@eventos.route("/update/<string:id>", methods=["GET", "POST"])
def update(id):

    Evento = Evento.query.get(id)

    if request.method == "POST":
        Evento.nombre = request.form['nombre']
        Evento.fecha_inicio = request.form['fecha_inicio']
        Evento.fecha_fin = request.form['fecha_fin']

        db.session.commit()

        flash('¡Su evento ha sido actualizado correctamente!')

        return redirect(url_for('boletos.index'))

    return render_template("update.html", eventos=eventos)


@eventos.route("/delete/<id>", methods=["GET"])
def delete(id):
    Evento = Evento.query.get(id)
    db.session.delete(Evento)
    db.session.commit()

    flash('¡Su evento ha sido eliminado correctamente!')

    return redirect(url_for('eventos.index'))

@eventos.route("/vender_boleto")
def about():
    return render_template("")

@eventos.route("/canjear_boleto")
def about():
    return render_template("")

@eventos.route("/detalle_evento")
def about():
    return render_template("")


