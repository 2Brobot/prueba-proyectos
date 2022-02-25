pkg load database 
conn = pq_connect(setdbopts('dbname','postgres','host','localhost','port','5432','user','postgres','password','123'))
costo = input('Introduce el costo: ');
iva=costo*0.12
sin_iva=costo*0.88
N=pq_exec_params(conn, "insert into pexamen3 (costo, iva, sin_iva) values($1, $2, $3);",{costo,iva,sin_iva})