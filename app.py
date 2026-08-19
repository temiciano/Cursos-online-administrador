from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

DB_path = "cursos.db"

#definimos funciones
def get_cursos():
	conn=sqlite3.connect(DB_path)
	cursor=conn.cursor()
	cursor.execute('SELECT * FROM cursos')
	cursos=cursor.fetchall()
	conn.close()
	return cursos

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


#llamada a fnciones
@app.route('/')
def index():
	cursos = get_cursos()
	return render_template('index.html' , cursos=cursos)

if __name__ == '__main__':
	app.run(debug=True)