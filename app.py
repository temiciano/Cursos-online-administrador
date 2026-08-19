from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

DB_path = "cursos.db"

#------------ funciones de visualizacoin -------

def get_cursos():
	conn=sqlite3.connect(DB_path)
	cursor=conn.cursor()
	cursor.execute('SELECT * FROM cursos')
	cursos=cursor.fetchall()
	conn.close()
	return cursos

def get_participantes():
	conn = sqlite3.connect(DB_path)
	cursor = conn.cursor()
	cursor.execute("""
		SELECT participantes.id_participante,
		       participantes.nombre,
		       participantes.correo,
		       participantes.telefono,
		       participantes.institucion,
		       cursos.nombre
		FROM participantes
		JOIN inscripciones ON participantes.id_participante = inscripciones.id_participante
		JOIN cursos ON inscripciones.id_curso = cursos.id_curso
	""")
	participantes = cursor.fetchall()
	conn.close()
	return participantes

# -------- funciones de escritura -----------

@app.route('/nuevo', methods=['GET', 'POST'])
def nuevo_curso():
    if request.method == 'POST':
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        inicio = request.form['inicio']
        fin = request.form['fin']
        cupos_max = request.form['cupos_max']
        estado = request.form['estado']

        conn = sqlite3.connect('cursos.db')
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO cursos (nombre, descripcion, inicio, fin, cupos_max, estado)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (nombre, descripcion, inicio, fin, cupos_max, estado))
        conn.commit()
        conn.close()

        return redirect('/')

    return render_template('nuevo_curso.html')

@app.route('/participante', methods=['GET', 'POST'])
def nuevo_participante():
    conn = sqlite3.connect('cursos.db')
    cursor = conn.cursor()
    if request.method == 'POST':
        rut = request.form['rut']
        nombre = request.form['nombre']
        correo = request.form['correo']
        telefono = request.form['telefono']
        institucion = request.form['institucion']
        id_curso = request.form['id_curso']

        cursor.execute("""
            INSERT INTO participantes (rut, nombre, correo, telefono, institucion)
            VALUES (?, ?, ?, ?, ?)
        """, (rut, nombre, correo, telefono, institucion))

        id_participante = cursor.lastrowid

        cursor.execute("""
            INSERT INTO inscripciones (id_curso, id_participante, estado)
            VALUES (?, ?, ?)
        """, (id_curso, id_participante, 'confirmado'))

        conn.commit()
        conn.close()
        return redirect('/')

    cursor.execute("SELECT id_curso, nombre FROM cursos WHERE estado = 'abierto'")
    cursos = cursor.fetchall()
    conn.close()
    return render_template('nuevo_participante.html', cursos=cursos)

@app.route('/')
def index():
	cursos = get_cursos()
	participantes = get_participantes()
	return render_template('index.html', cursos=cursos, participantes=participantes)

if __name__ == '__main__':
	app.run(debug=True)