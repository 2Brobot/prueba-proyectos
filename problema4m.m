pkg load database 
conn = pq_connect(setdbopts('dbname','postgres','host','localhost','port','5432','user','postgres','password','123'))
numero = input('Introduce el numero a evaular: ');
contador=0
for i=1:numero
r=mod(numero,i)
if(r==0)
contador=1+contador
endif
endfor
if (contador<=2)
tipo="primo"
disp("Es primo")
N=pq_exec_params(conn, "insert into pexamen4 (numero, tipo) values($1, $2);",{numero,tipo})
endif
if (contador>2)
disp("Es compuesto---------------aaa------------------")
tipo="compuesto"
N=pq_exec_params(conn, "insert into pexamen4 (numero, tipo) values($1, $2);",{numero,tipo})
endif
