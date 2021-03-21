# Conversão do Tempo #1019

# Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma fábrica, e informe-o expresso no formato horas:minutos:segundos.

tempo = int(input())
segundo = tempo % 60
minutos = tempo / 60
minuto = minutos % 60
hora = minutos / 60

print('{0:.0f}'.format(hora),':','{0:.0f}'.format(minuto),':','{0:.0f}'.format(segundo))v
