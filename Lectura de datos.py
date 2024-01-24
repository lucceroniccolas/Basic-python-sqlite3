import sqlite3 as sql

def read_data():

    conn = sql.connect("Sistema_de_mesas_de_examenes.db")
    cursor = conn.cursor()




    
    # Leer datos de la tabla 'Estudiantes'
    cursor.execute('''
        SELECT * FROM Estudiantes
    ''')
    



    # Obtener todos los registros
    rows = cursor.fetchall()



    # Imprimir los datos (esto puede variar dependiendo de tus necesidades)
    for row in rows:
        print(row)


    #Leer datos de la tabla 



    conn.close()



if __name__ == "__main__": 
    
    
    read_data()