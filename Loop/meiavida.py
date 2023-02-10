s , m = map(int,input().split(" "))

contador=0
for i in range (s):
    while (m>=0.5):
        m = m /2
        contador = contador + 1
    segundos=contador*s

dias = segundos // 86400
segundos_rest = segundos % 86400
horas = segundos_rest // 3600
segundos_rest = segundos_rest % 3600
minutos = segundos_rest // 60
segundos_rest = segundos_rest % 60

print(dias,"dias","{:02d}",":","{:02d}",":","{:02d}".format(horas,minutos,segundos_rest))

