# Cédulas  #1018

# Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas) no qual o valor pode ser decomposto. 
# As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1. 
# A seguir mostre o valor lido e a relação de notas necessárias.

valor = int(input())
print(valor)

n100 = valor//100
valor = valor - n100*100

n50 = valor//50
valor = valor - n50*50

n20 = valor//20
valor = valor - n20*20

n10 = valor//10
valor = valor - n10*10

n5 = valor//5
valor = valor - n5*5

n2 = valor//2
valor = valor - n2*2

n1 = valor//1
valor = valor - n1*1

print('{} nota(s) de R$ 100,00'.format(n100))
print('{} nota(s) de R$ 50,00'.format(n50))
print('{} nota(s) de R$ 20,00'.format(n20))
print('{} nota(s) de R$ 10,00'.format(n10))
print('{} nota(s) de R$ 5,00'.format(n5))
print('{} nota(s) de R$ 2,00'.format(n2))
print('{} nota(s) de R$ 1,00'.format(n1))
