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


#Questão 5

nota1 = float(input("Digite a sua primeira nota:"))
nota2 = float(input("Digite a sua primeira nota:"))

media = (nota1 + nota2) / 2
conceito = ''

if media <= 10 and media >= 9:
    conceito = 'A'
elif media < 9 and media >= 7.5:
    conceito = 'B'
elif media < 7.5 and media >= 6:
    conceito = 'C'
elif media < 6 and media >= 4:
    conceito = 'D'
elif media < 4 and media >= 0:
    conceito = 'E'

if conceito in ['A', 'B', 'C']:
    status = 'APROVADO'
else:
    status = 'REPROVADO'

print("Informações do Aluno:")
print(f"Notas: {nota1} e {nota2}")
print(f"Média: {media}")
print(f"Conceito: {conceito}")
print(f"Status: {status}")


#Questão 6

ano = int(input('Digite o ano: '))

if ano % 4 == 0:
    print('Ano bissexto')
else:
    print('Ano não é bissexto')


#Questão 7 

print("Calculadora")
num1 = float(input("Digite o primeiro número:"))
num2 = float(input("Digite o segundo número:"))
escolha = int(input("\n1- Soma\n2- Sub\n3- Multiplicação\n4- Divisão\n5- Exponenciação\nOperação:"))

paridade = ''
sinal = ''
natu = ''

def soma(a, b):
    return a + b 
def sub(a, b):
    return a - b 
def mult(a, b):
    return a * b 
def div(a, b):
    return a / b 
def exp(a, b):
    return a ** b 

if escolha == 1:
    resultado = soma(num1, num2)
elif escolha == 2:
    resultado = sub(num1, num2)
elif escolha == 3:
    resultado = mult(num1, num2)
elif escolha == 4:
    if num2 == 0:
        print("Impossível dividir por 0.")
    else:
        resultado = div(num1, num2)
elif escolha == 5:
    resultado = exp(num1, num2)

if resultado % 2 == 0:
    paridade = 'Par'
else:
    paridade = 'Ímpar'

if resultado >= 0:
    sinal = 'Positivo'
else:
    sinal = 'Negativo'

if resultado == int(resultado):
    natu = 'Inteiro'
else:
    natu = 'Decimal'

print(f"Resultado: {resultado}")
print(f"O resultado é {paridade}, {sinal} e {natu}.")    


#Questão 8

idade = int(input('Digite sua idade:'))
 
if idade < 0 or idade > 150:    
    print('Idade inválida! \nValores aceitáveis apenas entre 0 e 150!')
else:
    print(f'Sua idade é: {idade}')


#Questão 9

#Com o .append

nums = []
cont = 0
 
while cont != 5:
   
    num = int(input('Digite um número:'))
    nums.append(num)
    soma = sum(nums)
    media = sum(nums) / len(nums)
 
    cont += 1
 
print("O resultado da soma dos números:", soma)
print("A média dos números:", media)
 
#Sem o .append
 
tamanho_lista = 5
nums = [0] * tamanho_lista
cont = 5
 
while cont < tamanho_lista:
    num = int(input("Digite um número:"))
    nums[cont] = num
    cont += 1
 
soma = sum(nums)
media = soma / tamanho_lista
 
print("O resultado da soma dos números:", soma)
print("A média dos númeors:", media)


#Questão 10

num = int(input("Digite um número inteiro:"))
 
primo = True
 
if num <= 1:
    primo = False
else:
    for n in range(2, num):
        if num % n == 0:
            primo = False
            break

if primo:
    print("É um número Primo")
else:
    print("Não é um número Primo")


#Questão 11

temps = []
cont = 0

print("Digite 5 temperaturas")

while cont != 5:
    temp = float(input(f"Informe a {cont + 1}º temperatura:"))
    temps.append(temp)
 
    cont += 1

temp_min = min(temps)
temp_max = max(temps)
media = sum(temps) / cont
 
print('Temperaturas informadas:', temps)
print('Maior temperatura:', temp_max)
print('Menor temperatura:', temp_min)
print('A média das temperaturas:', media)


#Questão 12

saldo = float(input("Digite seu saldo médio:"))

if saldo <= 0:
    print("Valor inválido! \nImpossível calcular o valor do crédito")

elif saldo > 0 and saldo <= 200:
    print(f"Seu saldo médio é de: {saldo} reais.")
    print("Você não possui nenhum crédito.")

elif saldo >= 201 and saldo <= 400:
    credito = saldo * 0.2   
    print(f"Seu saldo médio é de: {saldo} reais.")
    print(f"Você possui {credito} reais de crédito")

elif saldo >= 401 and saldo <= 600:
    credito = saldo * 0.3
    print(f"Seu saldo médio é de: {saldo} reais.")
    print(f"Você possui {credito} reais de crédito")

else:
    credito = saldo * 0.4
    print(f"Seu saldo médio é de: {saldo} reais.")
    print(f"Você possui {credito} reais de crédito")


#Questão 13

import datetime

ano_atual = datetime.datetime.now().year

nome = str(input("Digite seu nome:"))
idade = int(input("Digite sua idade:"))

ano_nasc = ano_atual - idade
ano_aposentadoria = ano_nasc + 65

if idade >= 65:
    print(f"Sr/Sra {nome}, você já pode se aposentar")
elif ano_aposentadoria > ano_atual:
    print(f"Sr/Sra {nome}, você poderá se aposentar em {ano_aposentadoria}")


#Questão 14

valor_hora = float(input("Informe o valor da sua hora:"))
quant_horas = float(input("Informe a quantidade de horas trabalhadas no mês:"))

salario_bruto = valor_hora * quant_horas
desc_sind = salario_bruto * 0.03
fgts = salario_bruto * 0.11

if salario_bruto <= 2112.00:
    desc_ir = 0
elif salario_bruto >= 2112.01 and salario_bruto <= 2826.65:
    desc_ir = salario_bruto * 0.075
elif salario_bruto >= 2826.66 and salario_bruto <= 3751.05:
    desc_ir = salario_bruto * 0.15
elif salario_bruto >= 3751.06 and salario_bruto <= 4664.68:
    desc_ir = salario_bruto * 0.225
elif salario_bruto > 4664.68:
    desc_ir = salario_bruto * 0.275

salario_liquido = salario_bruto - desc_ir - desc_sind

print("__Folha de Pagamento__")
print("Salário bruto:", salario_bruto)
print("Desconto do IR:", desc_ir)
print("Sindicato:", desc_sind)
print("FGTS:", fgts)
print("Salário líquido:", salario_liquido)
