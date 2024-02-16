import sqlite3 as sql
from datetime import datetime, timezone
import random

#########
#CARRERA#
#########

def crear_carrera(nombre, duracion):
    conn=sql.connect("Sistema_de_mesas_de_examentes.db")
    cursor=conn.cursor()
    cursor.execute("""INSERT INTO Carrera(Nombre_de_carrera,Duracion)
                   VALUES (?,?)""",(nombre,duracion))
    cursor.execute("""SELECT last_insert_rowid()""") 
    carrera_id=cursor.lastrowid
    conn.commit()
    conn.close()
    print (carrera_id)
    return(carrera_id)

#########
#ALUMNOS#
#########

def insert_alumnos_y_inscripcion(Nombre, Apellido, DNI, Direccion, Telefono, Correo):
    conn=sql.connect("Sistema_de_mesas_de_examentes.db")
    cursor=conn.cursor()

### Insertamos datos en la tabla 'Alumnos' usando variables de python 

    cursor.execute("""INSERT INTO estudiantes(Nombre, Apellido, DNI, Direccion, Telefono, Correo)
                   VALUES (?,?,?,?,?,?)""", (Nombre, Apellido, DNI, Direccion, Telefono, Correo))
     
    #Obtenemos el id del ultimo alumno insertado 

    cursor.execute("""SELECT last_insert_rowid()""")
    alumno_id=cursor.lastrowid
    conn.commit()
    conn.close()

    return (alumno_id)  

#########
#MATERIA#
#########

def insert_materia(id_carrera,materia,descripcion):
    conn=sql.connect("Sistema_de_mesas_de_examentes.db")
    cursor =conn.cursor()

    #Insertamos datos en la tabla Materia usando variables de python
    cursor.execute("""INSERT INTO materia (Id_Carrera,Nombre_materia, Descripcion)
                   VALUES (?,?,?)""",(id_carrera,materia,descripcion))

    cursor.execute("""SELECT last_insert_rowid()""")
    materia_id=cursor.lastrowid
    conn.commit()
    conn.close()
    print (materia_id)
    return(materia_id)

######
#MESA#
######

def insertar_mesa(id_materia,Fecha_y_hora_str,Profesor_titular,Primer_vocal,Segundo_vocal,Tercer_vocal,Aula,Duracion):
 
    conn=sql.connect("Sistema_de_mesas_de_examentes.db")
    cursor=conn.cursor()

 # Convertir la cadena de fecha y hora a un objeto datetime
    Fecha_y_hora_objeto= datetime.strptime(Fecha_y_hora_str,"%Y-%m-%d %H:%M:%S")

   # print(type(Fecha_y_hora_objeto))
# Obtener el timestamp UNIX
    #timestamp_fecha_y_hora=int(Fecha_y_hora_objeto.timestamp())

    cursor.execute("""INSERT INTO Mesa_de_examen(Id_materia, Fecha_y_hora,Profesor_titular, Primer_vocal, Segundo_vocal, Tercer_vocal, Aula, Duracion)
                   VALUES (?, ?, ?, ?, ?, ?, ?,?)""",(id_materia, Fecha_y_hora_str,Profesor_titular, Primer_vocal, Segundo_vocal, Tercer_vocal, Aula, Duracion))

    cursor.execute("""SELECT last_insert_rowid()""")
    mesa_id=cursor.lastrowid

    conn.commit()
    conn.close()  
    
    return (mesa_id)

#############
#INSCRIPCION#
#############

def inscribir_alumno_en_mesa(id_estudiante,id_mesa):
    conn=sql.connect("Sistema_de_mesas_de_examentes.db" )
    cursor=conn.cursor()

    tiempo_real=datetime.now().timestamp()
   # print(type(tiempo_real))
    
    # Convierte el timestamp UNIX a un objeto datetime consciente del huso horario (UTC)
    fecha_hora_objeto_utc = datetime.fromtimestamp(tiempo_real, timezone.utc)
  #  print(type(fecha_hora_objeto_utc))
    
    # Formatea la fecha y hora en un formato legible
    formato_legible = fecha_hora_objeto_utc.strftime("%Y-%m-%d %H:%M:%S")
 #   print(type(formato_legible))
#datetime.now().timestamp())
    
    cursor.execute("""INSERT INTO inscripcion(Id_estudiante,Id_mesa,Fecha_Inscripcion)
                   VALUES (?,?,?)""",(id_estudiante,id_mesa,formato_legible))
    conn.commit() 
    conn.close()

################
#ACTA_DE_EXAMEN#
################
    
def notas(id_estudiante,nota_oral,id_mesa,nota_escrito,):
    conn=sql.connect("Sistema_de_mesas_de_examentes.db" )
    cursor=conn.cursor()

    nota_final=0
    nota_final= nota_escrito + nota_oral
    nota_final=nota_final/2

    cursor.execute("""INSERT INTO Acta_de_Examen(Id_estudiante,Nota_oral,Id_mesa,Nota_escrito,Nota_final)
                   VALUES (?,?,?,?,?)""",(id_estudiante,nota_oral,id_mesa,nota_escrito,nota_final))
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
   
    ## CREAMOS CARRERA

    id_carrera=crear_carrera("DESARROLLO DE SOFTWARE",3)
    
    ### CREAMOS MATERIAS

    id_materia1=insert_materia(id_carrera,"BASE DE DATOS", "Segundo año - Mesa de Febrero")
    id_materia2=insert_materia(id_carrera,"PROGRAMACION","Segundo año - Mesa de Febrero")

    
    ## CREAMOS ALUMNO
    alumno_id=insert_alumnos_y_inscripcion("Diego","Rodriguez",43213563,"Barrio Fenca",2622123321,"diegordz@gmail.com")
    alumno_id2=insert_alumnos_y_inscripcion("Candelaria","Mass",45623876,"Barrio catulo",262244343,"quiandets@gmail.com")
    alumno_id3=insert_alumnos_y_inscripcion("Nicolas","Lucero",44878464,"Barrio San Antonio",2622587300,"nicolashdgg@gmail.com")
    alumno_id4=insert_alumnos_y_inscripcion("Franco","Tello",42234654,"Barrio San catulo",2622237854,"francoviach@gmail.com")


     ## CREAMOS MESAS
    mesa_id=insertar_mesa(id_materia1,"2024-02-15 19:30:00","Diego Lobos","Diego Lobos","Gabriel Fuertes","Martin Aristiaram",6,1)   
    mesa_id2=insertar_mesa(id_materia2,"2024-02-15 19:00:00","Martin Aristiaram","Martin Aristiaram","","",7,1)
   
   
    ## INSCRIBIMOS ALUMNOS A MESAS CORRESPONDIENTES ##

    inscribir_alumno_en_mesa(alumno_id,mesa_id)
    inscribir_alumno_en_mesa(alumno_id2,mesa_id)
    inscribir_alumno_en_mesa(alumno_id3,mesa_id)
    inscribir_alumno_en_mesa(alumno_id4,mesa_id2)
    
    ## colocamos notas ##
    
    

    notas(alumno_id,random.randint(0,10),mesa_id,random.randint(0,10))
    notas(alumno_id2,random.randint(0,10),mesa_id,random.randint(0,10))
    notas(alumno_id3,random.randint(0,10),mesa_id,random.randint(0,10))
    notas(alumno_id4,random.randint(0,10),mesa_id2,random.randint(0,10))


