pkg load database
conn = pq_connect(setdbopts('dbname','postgres','host','localhost','port','5432','user','postgres','password','123'))
n1=randi(6)
n2=randi(6)
suma=n1+n2
if(suma==8)
disp("Ganaste");
resultado="ganaste"
N=pq_exec_params(conn, "insert into pexamen1 (dado1, dado2, resultado) values($1, $2, $3);",{n1,n2,resultado})
elseif(suma==7)
disp("Perdiste");
resultado="perdiste"
N=pq_exec_params(conn, "insert into pexamen1 (dado1, dado2, resultado) values($1, $2, $3);",{n1,n2,resultado})
elseif(suma!=8 && suma!=7)
disp("Sigue jugando") 
resultado="otro turno"
N=pq_exec_params(conn, "insert into pexamen1 (dado1, dado2, resultado) values($1, $2, $3);",{n1,n2,resultado})
endif