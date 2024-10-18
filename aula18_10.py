#Durante a aula
palavra = 'tranquilo'

for indice, letra in enumerate(palavra):
    print(indice, letra)

#Questão 1
letra = input('Digite uma letra:')

if (letra in 'AaEeIiOoUu'):
    print('A letra que você digitou é uma vogal')
else:
    print('A letra que você digitou é uma consoante')

#Questão 2
produto1 = float(input('Qual o valor do primeiro produto:'))
produto2 = float(input('Qual o valor do segundo produto:'))
produto3 = float(input('Qual o valor do terceiro produto:'))

if (produto1 < produto2 and produto1 < produto3):
    print('O melhor produto para se comprar é o produto 1.')
elif (produto2 < produto1 and produto2 < produto3):
    print('O melhor produto para se comprar é o produto 2.')
else:
    print('O melhor produto para se comprar é o produto 3.')

#Questão 3
#Sem métodos:
num1 = int(input('Digiteo primeiro número:'))
num2 = int(input('Digiteo segundo número:'))
num3 = int(input('Digiteo terceiro número:'))

if num1 > num2 and num1 > num3 and num3 > num2:
    print("A ordem decrescente é", num1, num3, num2)

elif num1 > num2 and num1 > num3 and num2 > num3:
    print("A ordem decrescente é", num1, num2, num3)
 
elif num2 > num1 and num2 > num3 and num1 > num3:
    print("A ordem decrescente é", num2, num1, num3)

elif num2 > num1 and num2 > num3 and num3 > num1:
    print("A ordem decrescente é", num2, num3, num1)

elif num3 > num1 and num3 > num2 and num1 > num2:
    print("A ordem decrescente é", num3, num1, num2)

elif num3 > num1 and num3 > num2 and num2 > num1:
    print("A ordem decrescente é", num3, num2, num1)

#Com métodos:
num1 = int(input('Digiteo primeiro número:'))
num2 = int(input('Digiteo segundo número:'))
num3 = int(input('Digiteo terceiro número:'))

numeros = [num1, num2, num3]
numeros.sort(reverse=True)
print(numeros)

#Questão 4
print('Qual o seu turno?')
turno = input('Digite M- matutino, V- vesperino ou N- noturno:')

if (turno in 'Mm'):
    print("Bom Dia!")

elif (turno in 'Vv'):
    print("Bom Tarde!")

elif (turno in 'Nn'):
    print("Bom Noite!")

else:
    print('Valor Inválido!')