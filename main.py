from flask import Flask, render_template, request, redirect, url_for
import repositoriolibros as repo
import json

app = Flask(__name__)

@app.route("/")
def index():
    return "Hola Mundo!!"

@app.route("/autor")
def firtautor():
    autor = repo.selectFirstAutor()
    return json.dumps(autor)

@app.route("/autores/listado")
def listadeautores():
    autores = repo.selectAllAutor()
    return render_template('listautores.html', titulo = "Lista autores", lista_autores = autores)

@app.route("/autores/nuevo", methods=('GET','POST'))
def nuevoautor():
    if request.method == 'GET':
        return render_template('altautor.html')
    else: # significa que es post
        codigo = request.form['codigo']
        nombre = request.form['nombre']
        return redirect('/autores/listado')

@app.route("/autores/editar/<int:id>", methods=('GET',  'POST'))
def editarautor(id):
    pass

@app.route("/autores/borrar/<int:id>", methods=('GET',  'POST'))
def borrarautor(id):
    pass