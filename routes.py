from app import app, db
from flask import render_template, redirect, url_for, request
import formularios
from models import Tarea


@app.route('/')
@app.route('/index')
def index():
        return render_template('index.html', subtitulo = "Actidad en grupo TAI")

@app.route('/sobrenosotros', methods=['GET', 'POST'])
def sobrenosotros():
    formulario = formularios.FormAgregarTareas()

    # CREATE
    if formulario.validate_on_submit():
        nueva = Tarea(
            titulo=formulario.titulo.data,
            descripcion=formulario.descripcion.data
        )
        db.session.add(nueva)
        db.session.commit()
        return redirect(url_for('sobrenosotros'))

    tareas = Tarea.query.order_by(Tarea.id.desc()).all()
    total = Tarea.query.count()

    return render_template(
        'sobrenosotros.html',
        form=formulario,
        tareas=tareas,
        total=total
    )

@app.route('/completar/<int:id>')
def completar(id):
    tarea = Tarea.query.get_or_404(id)
    tarea.completada = not tarea.completada
    db.session.commit()
    return redirect(url_for('sobrenosotros'))


    
@app.route('/saludo')
def saludo():
        return 'Hola bienvenido a Taller Apps '
    
@app.route('/usuario/<nombre>')
def usuario(nombre):
        return f'Hola{nombre} bienvenido a Taller Apps '
