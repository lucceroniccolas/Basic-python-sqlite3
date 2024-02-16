import sqlite3 as sql
from datetime import datetime, timezone
def suprimir_datos_id(id):
    conn= sql.connect("Sistema_de_mesas_de_examentes.db")
    cursor=conn.cursor()

    #Eliminamos datos
    cursor.execute("""DELETE FROM estudiantes WHERE Id=? """, (id,))
    conn.commit()
    conn.close()

def mostrar_id_y_nombres():
    
    conn = sql.connect("Sistema_de_mesas_de_examentes.db")
    cursor = conn.cursor()
    cursor.execute("""SELECT Id,Nombre,Apellido FROM estudiantes """)

    datos=cursor.fetchall()

    for dato in datos:
        print ("ID :", dato[0])
        print ("Nombre :", dato[1])
        print ("Apellido :", dato[2])
        print("----------------")
    
    conn.close()

def nota_de_alumnos(nombre,apellido):

    conn = sql.connect("Sistema_de_mesas_de_examentes.db")
    cursor = conn.cursor()
 
    # La cláusula JOIN combina las filas de ambas tablas alumnos y acta_de_examen basándose en el id del alumno usando la clausula where para determinar que usando determinados valores (nombre y apellido) solicitamos la nota final
   
    consulta=("""SELECT Estudiantes.Nombre, Estudiantes.Apellido, Acta_de_examen.Nota_final FROM estudiantes JOIN Acta_de_Examen ON estudiantes.Id = Acta_de_Examen.Id_estudiante WHERE estudiantes.Nombre ||' '|| estudiantes.Apellido = ?""")

    cursor.execute(consulta,(nombre + ' ' + apellido,))

    resultados=cursor.fetchall()
    for resultado in resultados:
        print(f"Nombre:{resultado[0]}, Apellido: {resultado[1]}, Nota final: {resultado[2]}")
    
    #Cerramos conexión
    conn.close()

 
def fecha_de_mesas(): 
    conn = sql.connect("Sistema_de_mesas_de_examentes.db")
    cursor = conn.cursor()
    cursor.execute("""SELECT materia.Nombre_materia, Mesa_de_examen.Fecha_y_hora FROM materia JOIN Mesa_de_examen ON materia.Id = Mesa_de_examen.Id_materia""")

    resultados=cursor.fetchall()

    conn.commit()
    for materia, mesa in resultados:
        print(f"La materia {materia} tiene la mesa la fecha {mesa}")
    
    conn.close()

if __name__ == "__main__": 
    respuesta=9
    while respuesta!=0 :

        respuesta=int(input("\n ¿Qué consulta desea realizar? \n \n 0. Exit  \n 1. ¿Cuáles son los id de los alumnos? \n 2. Borrar a alguien de la lista mediante id \n 3. ¿Cuáles Son las notas finales? \n 4. ¿Cuándo son las mesas?  \n   "))
    
        if respuesta==1: 
            mostrar_id_y_nombres()

        elif respuesta==2:
            elid=int(input("Ingrese el id que desea eliminar"))
            suprimir_datos_id(elid)

        elif respuesta==3:
            nombre= input("Ingrese el nombre del alumno:    ")
            apellido=input("Ingrese el apellido del alumno:   ")
            nota_de_alumnos(nombre,apellido)
        elif respuesta==4:
            fecha_de_mesas()
       