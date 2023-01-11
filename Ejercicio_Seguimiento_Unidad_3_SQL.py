import sqlite3 as s3

# CONSULTAS SQL.
"""
Resuelve las siguientes consultas SELECT sobre la base de datos de libros:

Obtén el título y año de aquellos libros cuyo año sea mayor de 2002.
Cuenta cuántos libros tienen el autor de nombre "Rem Koolhaas"
Obtén, a la vez, el menor y mayor año (columna anho) de los libros.
Obtén el isbn de aquellos libros cuyo autor tenga un nombre que comience por la palabra "Varios" """

def libros_anho_mayores_2022():

    conexion = s3.connect("libros.db")
    cursor = conexion.cursor()
    cursor.execute('select libros.titulo, libros.anho from libros where libros.anho > 2022')
    libros = cursor.fetch()
    cursor.close()
    conexion.close()
    return libros

def cuenta_libros_autor():

    conexion = s3.connect("libros.db")
    cursor = conexion.cursor()
    cursor.execute("select count(*) from autores join libros on autores.id=libros.autor where autores.Nombre == 'Rem Koolhaas' ")
    libros = cursor.fetchone()
    cursor.close()
    conexion.close()
    return libros[0]

def max_min_anhos_libros():

    conexion = s3.connect("libros.db")
    cursor = conexion.cursor()
    cursor.execute("select min(libros.anho),max(libros.anho) from libros")
    min_max = cursor.fetchone()
    cursor.close()
    conexion.close()
    return min_max

def select_libros_autor_varios():

    conexion = s3.connect("libros.db")
    cursor = conexion.cursor()
    cursor.execute("select isbn from libros where autores.nombre like 'Varios%'")
    isbn = cursor.fetch()
    cursor.close()
    conexion.close()
    return isbn

def average_anho():

    conexion = s3.connect("libros.db")
    cursor = conexion.cursor()
    cursor.execute("select avg(numLibros) from ResumenAutores")
    avg = cursor.fetchone()
    cursor.close()
    conexion.close()
    return avg[0]