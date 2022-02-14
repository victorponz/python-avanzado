import sqlite3;
mi_conexion = sqlite3.connect("./voluntarios/ejers_voluntarios_ejer2.db")
mi_cursor = mi_conexion.cursor()
ins = """INSERT INTO LISTA_HERRAMIENTAS
    VALUES('ana' , 'alas')
"""
mi_cursor.execute(ins)

ins = """INSERT INTO LISTA_HERRAMIENTAS
VALUES(?, ?)"""
mi_cursor.execute(ins, ("ana", "botines"))

lista = [('ana', 'ratrillo'),
        ('pep', 'alas'),
        ('pep', 'varita'),
        ('mary', 'varita'),
        ('mary', 'esencia'),
        ('mary', 'martillo'),
        ('quico', 'botines'),
        ('quico', 'ratrillo'),
        ('sandy', 'varita')]
mi_cursor.executemany(ins, lista)

mi_conexion.commit()
mi_conexion.close()