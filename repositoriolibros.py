import sqlite3 as s3

def select_libros():

    conexion = s3.connect("libros.db")
    cursor = conexion.cursor()
    cursor.execute('select libros.titulo, libros.anho from libros where libros.anho > 2022')
    libros = cursor.fetch()
    cursor.close()
    conexion.close()
    return libros

def cuantos_libros():

    conexion = s3.connect("libros.db")
    cursor = conexion.cursor()
    cursor.execute("select count(*) from autores join libros on autores.id=libros.autor where autores.Nombre == 'Rem Koolhaas' ")
    libros = cursor.fetchone()
    cursor.close()
    conexion.close()
    return libros[0]

def select_libros():

    conexion = s3.connect("libros.db")
    cursor = conexion.cursor()
    cursor.execute("select min(libros.anho),max(libros.anho) from libros")
    min_max = cursor.fetchone()
    cursor.close()
    conexion.close()
    return min_max

def select_libros():

    conexion = s3.connect("libros.db")
    cursor = conexion.cursor()
    cursor.execute("select isbn from libros where autores.nombre like 'Varios%'")
    isbn = cursor.fetch()
    cursor.close()
    conexion.close()
    return isbn

def average():

    conexion = s3.connect("libros.db")
    cursor = conexion.cursor()
    cursor.execute("select avg(numLibros) from ResumenAutores")
    avg = cursor.fetchone()
    cursor.close()
    conexion.close()
    return avg[0]


def selectAllAutor():

    conexion = s3.connect("libros.db")
    cursor = conexion.cursor()
    cursor.execute('select * from autores')
    autores = cursor.fetchall()
    cursor.close()
    conexion.close()
    return autores

def selectFirstAutor():

    conexion = s3.connect("libros.db")
    cursor = conexion.cursor()
    cursor.execute('select * from autores')
    autores = cursor.fetchone()
    cursor.close()
    conexion.close()
    return autores

def deleteAutor(id):

    conexion = s3.connect("libros.db")
    cursor = conexion.cursor()
    cursor.execute('delete from autores where id = ?',(id,))
    conexion.commit()
    cursor.close()
    conexion.close()
    return cursor.rowcount == 1

def updateAutor(id,nombre):

    conexion = s3.connect("libros.db")
    cursor = conexion.cursor()
    cursor.execute('update autores set nombre = ? where id = ?',(nombre,id))
    conexion.commit()
    cursor.close()
    conexion.close()
    return cursor.rowcount == 1

def findtAutor(id):

    conexion = s3.connect("libros.db")
    cursor = conexion.cursor()
    cursor.execute('select id, nombre from autores where id = ?',(id,))
    autores = cursor.fetchone()
    cursor.close()
    conexion.close()
    return autores