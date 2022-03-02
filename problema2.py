import statistics
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

def insertar(n1,n2,n3,n4,n5,media,mediana,moda,rango,desviacion,varianza):
    cursor = conexion.cursor() 
    cursor.execute("INSERT INTO pexamen2(n1,n2,n3,n4,n5,media,mediana,moda,rango,desviacion,varianza) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);",(n1,n2,n3,n4,n5,media,mediana,moda,rango,desviacion,varianza))
    conexion.commit()
    print('Datos incertados correctamente')
x=0
##comentario x=1
while x==0:
    print('ingrese 1 para notas')
    print('ingrese 2 para historial')
    comando=input()
    if comando=='1':
        x=1
        n1 = int(input("Ingrese la nota 1: "))
        n2 = int(input("Ingrese la nota 2: "))
        n3 = int(input("Ingrese la nota 3: "))
        n4 = int(input("Ingrese la nota 4: "))
        n5 = int(input("Ingrese la nota 5: "))
        notas = [n1,n2,n3,n4,n5]
        media=(n1+n2+n3+n4+n5)/5
        mediana=statistics.median(notas)
        moda=statistics.mode(notas)
        rango=max(notas)-min(notas)
        desviacion=statistics.pstdev(notas)
        varianza=statistics.pvariance(notas)
        insertar(n1,n2,n3,n4,n5,media,mediana,moda,rango,desviacion,varianza)
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