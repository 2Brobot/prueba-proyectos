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

def insertar(numero,tipo):
    cursor = conexion.cursor() 
    cursor.execute("INSERT INTO pexamen4(numero, tipo) VALUES(%s,%s);",(numero,tipo))
    conexion.commit()
    print('Datos incertados correctamente')
## Comentario
x=0
while x==0:
    print('1. ingresar')
    print('2. consultar')
    comando=input("ingresa el comando: ") 
    if comando=='1':
        x=1
        numero=int(input("Ingrese el numero: "))
        contador=0
        for n in range(1,numero+1):
             if (numero%n==0):
                  contador=contador+1
        if (contador==2) or (numero==1):
            print('EL numero es primo')
            tipo='primo'
            insertar(numero,tipo)
            x=0
        else:
            print('El numero no es primo')
            tipo='compuesto'
            insertar(numero,tipo)
            x=0
    elif comando=='2':
        x=1
        sql = 'SELECT*FROM pexamen4;'
        cursor = conexion.cursor()
        cursor.execute(sql)
        valores = cursor.fetchall()
        print(valores)
        x=0
    else:
        print('comando invalido')