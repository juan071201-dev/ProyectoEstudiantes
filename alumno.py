from database import get_db_connection

def obtener_todos():
    conn = get_db_connection()
    alumnos = conn.execute('SELECT * FROM alumnos').fetchall()
    conn.close()
    return alumnos

def obtener_por_id(alumno_id):
    conn = get_db_connection()
    alumno = conn.execute('SELECT * FROM alumnos WHERE id = ?', (alumno_id,)).fetchone()
    conn.close()
    return alumno

def crear_alumno(nombre, apellido, aprobado, nota, fecha):
    conn = get_db_connection()
    conn.execute(
        'INSERT INTO alumnos (nombre, apellido, aprobado, nota, fecha) VALUES (?, ?, ?, ?, ?)',
        (nombre, apellido, aprobado, nota, fecha)
    )
    conn.commit()
    conn.close()

def actualizar_alumno(alumno_id, nombre, apellido, aprobado, nota, fecha):
    conn = get_db_connection()
    conn.execute(
        'UPDATE alumnos SET nombre = ?, apellido = ?, aprobado = ?, nota = ?, fecha = ? WHERE id = ?',
        (nombre, apellido, aprobado, nota, fecha, alumno_id)
    )
    conn.commit()
    conn.close()

def eliminar_alumno(alumno_id):
    conn = get_db_connection()
    conn.execute('DELETE FROM alumnos WHERE id = ?', (alumno_id,))
    conn.commit()
    conn.close()
