from flask import Flask, render_template, request, redirect, url_for, abort
from alumno import (
    obtener_todos, obtener_por_id, crear_alumno,
    actualizar_alumno, eliminar_alumno
)
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('listar_alumnos'))

@app.route("/alumnos")
def listar_alumnos():
    buscar = request.args.get("buscar", "").lower()
    filtro = request.args.get("filtro", "")
    alumnos = obtener_todos()

    if buscar:
        if buscar.isdigit():
            alumnos = [a for a in alumnos if str(a['id']) == buscar]
        else:
            alumnos = [a for a in alumnos if buscar in a['nombre'].lower()]
    
    if filtro == "aprobado":
        alumnos = [a for a in alumnos if a['aprobado']]
    elif filtro == "reprobado":
        alumnos = [a for a in alumnos if not a['aprobado']]

    return render_template("alumno/lista.html", alumnos=alumnos)



@app.route('/alumnos/<int:alumno_id>')
def ver_alumno(alumno_id):
    alumno = obtener_por_id(alumno_id)
    if not alumno:
        abort(404)
    return render_template('alumno/detalle.html', alumno=alumno)

@app.route('/alumnos/crear', methods=['GET', 'POST'])
def crear():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        aprobado = bool(request.form.get('aprobado'))
        nota = float(request.form['nota'])
        fecha = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        crear_alumno(nombre, apellido, aprobado, nota, fecha)
        return redirect(url_for('listar_alumnos'))
    return render_template('alumno/crear.html')

@app.route('/alumnos/editar/<int:alumno_id>', methods=['GET', 'POST'])
def editar(alumno_id):
    alumno = obtener_por_id(alumno_id)
    if not alumno:
        abort(404)

    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        aprobado = bool(request.form.get('aprobado'))
        nota = float(request.form['nota'])
        fecha = request.form['fecha']
        actualizar_alumno(alumno_id, nombre, apellido, aprobado, nota, fecha)
        return redirect(url_for('listar_alumnos'))

    return render_template('alumno/editar.html', alumno=alumno)

@app.route('/alumnos/eliminar/<int:alumno_id>', methods=['POST'])
def eliminar(alumno_id):
    eliminar_alumno(alumno_id)
    return redirect(url_for('listar_alumnos'))

if __name__ == '__main__':
    app.run(debug=True)


