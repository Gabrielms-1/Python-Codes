dias = int(input())
ano = dias//365
print(ano, 'ano(s)')
meses = dias % 365
mes = meses//30
print(mes, 'mes(es)')
dia = meses % 30
print(dia, 'dia(s)')
