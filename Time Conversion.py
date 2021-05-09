tempo = int(input())
segundo = tempo % 60
minutos = tempo / 60
minuto = minutos % 60
hora = minutos / 60

print('{0:.0f}'.format(hora),
      ':', '{0:.0f}'.format(minuto), ':',
      '{0:.0f}'.format(segundo))
