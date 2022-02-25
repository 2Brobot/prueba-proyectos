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

def insertar(costo,iva,sin_iva):
    cursor = conexion.cursor() 
    cursor.execute("INSERT INTO pexamen3(costo, iva, sin_iva) VALUES(%s,%s,%s);",(costo,iva,sin_iva))
    conexion.commit()
    print('Datos incertados correctamente')
x=0
while x==0:
    print('1. registrar')
    print('2. consultar')
    comando=input()
    if comando=='1':
        x=1
        costo=float(input("Ingrese el costo: "))
        iva=costo*0.12
        sin_iva=costo*0.88
        insertar(costo,iva,sin_iva)
        x=0
    elif comando=='2':
        x=1
        sql = 'SELECT*FROM pexamen2;'
        cursor = conexion.cursor()
        cursor.execute(sql)
        valores = cursor.fetchall()
        print(valores)
        x=0
    else:
        print('comando invalido')
        x=0

