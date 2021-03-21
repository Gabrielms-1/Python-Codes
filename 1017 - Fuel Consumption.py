tempo = int(input('Insert the time spent on the trip: '))
velmed = int(input('\nInsert the average speed of the trip : '))

litros = (tempo * velmed)/12
litros = float(litros)

print('\n{0:.3f}'.format(litros))
