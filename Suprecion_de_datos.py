import sqlite3 as sql


def suprimir_datos_nombres(nombre):
    conn= sql.connect("Sistema de mesas de examentes.db")
    cursor=conn.cursor()

    #Eliminamos datos
    cursor.execute("""DELETE FROM estudiantes WHERE Nombre=? """, (nombre,))
    conn.commit()
    conn.close()


if __name__=="__main__":


        ### Eliminar datos segun el nombre  
    suprimir_datos_nombres("jorge")