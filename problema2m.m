pkg load database 
conn = pq_connect(setdbopts('dbname','postgres','host','localhost','port','5432','user','postgres','password','123'))
n1 = input('Introduce la nota 1: ');
n2 = input('Introduce la nota 2: ');
n3 = input('Introduce la nota 3: ');
n4 = input('Introduce la nota 4: ');
n5 = input('Introduce la nota 5: ');
notas = [n1,n2,n3,n4,n5]
media=(n1+n2+n3+n4+n5)/5
mediana=median(notas)
moda=mode(notas)
rango=max(notas)-min(notas)
desviacion=std(notas)
varianza=var(notas)
N=pq_exec_params(conn, "insert into pexamen2 (n1, n2, n3, n4, n5, media, mediana, moda, rango, desviacion, varianza) values($1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11);",{n1, n2, n3, n4, n5, media, mediana, moda, rango, desviacion, varianza})
