import sqlite3 as sql
from datetime import datetime


def insert_alumnos_y_inscripcion(Nombre, Apellido, DNI, Direccion, Telefono, Correo):
    conn=sql.connect("Sistema de mesas de examentes.db")
    cursor=conn.cursor()

### Insertamos datos en la tabla 'Alumnos' usando variables de python 

    cursor.execute("""INSERT INTO estudiantes(Nombre, Apellido, DNI, Direccion, Telefono, Correo)
                   VALUES (?,?,?,?,?,?)""", (Nombre, Apellido, DNI, Direccion, Telefono, Correo))
    
    #Obtenemos el id del ultimo alumno insertado 

<<<<<<< HEAD
    cursor.execute("""SELECT last_insert_rowid()""")
    alumno_id=cursor.lastrowid
    conn.commit()
    conn.close()
  
=======
    cursor.execute("SELECT last_insert_rowid()")
    alumno_id=cursor.fetchall()[0]
    conn.commit()
    conn.close()
    print (alumno_id)
>>>>>>> 9fbd989c06c8b76e82d7ef21d240fa61e6e33b23
    return (alumno_id)

   # cursor.execute("""INSERT INTO inscripcion ()
         #   VALUES (?, ?, ?, ?)""", (estudiante_id,))
    

def insertar_mesa(Fecha_y_hora_str,Profesor_titular,Primer_vocal,Segundo_vocal,Tercer_vocal,Aula,Duracion):
 
    conn=sql.connect("Sistema de mesas de examentes.db")
    cursor=conn.cursor()

 # Convertir la cadena de fecha y hora a un objeto datetime
    Fecha_y_hora_objeto= datetime.strptime(Fecha_y_hora_str,"%Y-%m-%d %H:%M:%S")

# Obtener el timestamp UNIX
    #timestamp_fecha_y_hora=int(Fecha_y_hora_objeto.timestamp())



# insetamos datos en la tabla 
    cursor.execute("""INSERT INTO Mesa_de_examen(Fecha_y_hora,Profesor_titular, Primer_vocal, Segundo_vocal, Tercer_vocal, Aula, Duracion)
                   VALUES (?, ?, ?, ?, ?, ?, ?)""",(Fecha_y_hora_objeto.timestamp(),Profesor_titular, Primer_vocal, Segundo_vocal, Tercer_vocal, Aula, Duracion))

    
<<<<<<< HEAD
    cursor.execute("""SELECT last_insert_rowid()""")
    mesa_id=cursor.lastrowid
=======
    cursor.execute("SELECT last_insert_rowid()")
    mesa_id=cursor.fetchall()[0]
>>>>>>> 9fbd989c06c8b76e82d7ef21d240fa61e6e33b23

   
    conn.commit()
    conn.close()  
<<<<<<< HEAD
    
=======
    print (type(mesa_id))
>>>>>>> 9fbd989c06c8b76e82d7ef21d240fa61e6e33b23
    return (mesa_id)
    

def inscribir_alumno_en_mesa(id_estudiante,id_mesa):
    conn=sql.connect("Sistema de mesas de examentes.db")
    cursor=conn.cursor()

   

    cursor.execute("""INSERT INTO inscripcion(Id_estudiante,Id_mesa,Fecha_Inscripcion)
                   VALUES (?,?,?)""",(id_estudiante,id_mesa,datetime.now().timestamp()))
    conn.commit()
    conn.close()


if __name__ == "__main__":
   
    ## INSERTAMOS ALUMNO
    alumno_id=insert_alumnos_y_inscripcion("Diego","Rodriguez",42000000,"BarrioFenca",2622609098,"Diegote@gmail.com")

        ## CREAMOS UNA MESA

    mesa_id=insertar_mesa("2024-02-15 19:30:00","Diego Lobos","Diego Lobos","Gabriel Fuertes","Martin Aristiaram",6,1)

    inscribir_alumno_en_mesa(alumno_id,mesa_id)
