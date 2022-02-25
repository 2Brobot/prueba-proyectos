import random
import psycopg2

try:
    conexion = psycopg2.connect(
        host = "localhost",
        port = "5432",
        user = "postgres",
        password = "123",
        dbname = "postgres"
    )
    print("conexion correcta")
except psycopg2.Error as e:
    print("No se pudo conectar")

def insertar(dado1,dado2,resultado):
    cursor = conexion.cursor() 
    cursor.execute("INSERT INTO pexamen1(dado1, dado2, resultado) VALUES(%s,%s,%s);",(dado1,dado2,resultado))
    conexion.commit()
    print('Datos incertados correctamente')

x=0
while x==0:
    print('ingresa 1 para jugar')
    print('ingresa 2 para ver el historial')
    comando=input()
    if comando=='1':
        x=1
        dado1=random.randint(1, 6)
        dado2=random.randint(1, 6)
        suma=dado1+dado2
        print('dado 1 = ',dado1)
        print('dado 2 = ',dado2)
        print('suma = ',suma)
        if suma==8:
            print('ganaste')
            resultado='ganaste'
            insertar(dado1,dado2,resultado)
            x=0
        elif suma==7:
            print('Perdiste')
            resultado='perdiste'
            insertar(dado1,dado2,resultado)
            x=0
        else:
            print('Puedes volver a jugar')
            resultado='otro turno'
            insertar(dado1,dado2,resultado)
            x=0
    elif comando=='2':
        sql = 'SELECT*FROM pexamen1;'
        cursor = conexion.cursor()
        cursor.execute(sql)
        valores = cursor.fetchall()
        print(valores)
        x=0
    else:
        print('Ingresa un comando valido')
