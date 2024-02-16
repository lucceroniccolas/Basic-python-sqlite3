import sqlite3 as sql

def create_tables(): 
    conn = sql.connect("Sistema_de_mesas_de_examentes.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS estudiantes(

                    Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    Nombre TEXT NOT NULL,
                    Apellido TEXT NOT NULL,
                    DNI INTEGER NOT NULL,
                    Direccion TEXT,
                    Telefono NUMERIC,
                    Correo TEXT
    )""")
    
    cursor.execute("""CREATE TABLE IF NOT EXISTS Carrera(
                   Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                   Nombre_de_carrera TEXT, 
                   Duracion NUMERIC
    )""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS materia(
                    Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    Id_Carrera INTEGER NOT NULL,
                    Nombre_materia  TEXT,
                    Descripcion TEXT,
                    FOREIGN KEY(Id_Carrera) REFERENCES Carrera(Id)
    )""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS inscripcion(
                    Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    Id_estudiante INTEGER NOT NULL,
                    Id_mesa INTEGER NOT NULL,
                    Fecha_Inscripcion NUMERIC,
                    FOREIGN KEY(Id_estudiante) REFERENCES estudiantes(Id),
                    FOREIGN KEY(Id_mesa) REFERENCES Mesa_de_examen(Id)
    ) """)
    
    cursor.execute("""CREATE TABLE IF NOT EXISTS Mesa_de_examen(
                   Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                   Id_materia TEXT NOT NULL, 
                   Fecha_y_hora INTEGER NOT NULL,
                   Profesor_titular TEXT NOT NULL,
                   Primer_vocal TEXT NOT NULL,
                   Segundo_vocal TEXT,
                   Tercer_vocal TEXT, 
                   Aula NUMERIC,
                   Duracion NUMERIC,
                   FOREIGN KEY (Id_materia) REFERENCES materia(Id)
    )""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS Acta_de_Examen( 
                    Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    Id_estudiante INTEGER NOT NULL,
                    Nota_oral NUMERIC, 
                    Id_mesa INTEGER,
                    Nota_escrito NUMERIC,
                    Nota_final NUMERIC NOT NULL,
                    FOREIGN KEY(Id_estudiante) REFERENCES estudiantes(Id),
                    FOREIGN KEY(Id_mesa) REFERENCES Mesa_de_examen(Id) 
    )""")

    
    conn.commit()
    conn.close()

if __name__== "__main__":
    create_tables()