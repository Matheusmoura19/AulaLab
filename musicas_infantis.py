#Música dos patinhos

patinhos = 5

while patinhos != 0:
    if patinhos > 2:
        print(f" {patinhos} patinhos foram passear\n Além das montanhas para brincar\n A mamãe gritou: Quá, quá, quá, quá\n Mas só {patinhos - 1} patinhos voltaram de lá\n")
    if patinhos == 2:
        print(f" {patinhos} patinhos foram passear\n Além das montanhas para brincar\n A mamãe gritou: Quá, quá, quá, quá\n Mas só {patinhos - 1} patinho voltou de lá\n")
    if patinhos == 1:
        print(f" {patinhos} patinho foi passear\n Além das montanhas para brincar\n A mamãe gritou: Quá, quá, quá, quá\n Mas nenhum patinho voltou de lá\n")

    patinhos -= 1

print(" Poxa, a mamãe patinha ficou tão triste naquele dia\n Aonde será que estavam os seus filhotinhos?\n Mas essa história vai ter um final feliz\n Sabe por quê?\n")
print(" A mamãe patinha foi procurar\n Além das montanhas, na beira do mar\n A mamãe gritou: Quá, quá, quá, quá!\n E os cinco patinhos voltaram de lá")

#Música dos elefantes

elefantes = 1
incomodam = 'incomodam '

muita_gente = [3, 5, 7, 9]
muito_mais = [2, 4, 6, 8, 10]
muito_menos = [2, 4, 6, 8]

for n in range(1, 11):
    if elefantes == 1:
        print(f"{elefantes} elefante incomoda muita gente")
    if elefantes in muito_mais:
        print(f"{elefantes} elefantes {incomodam * elefantes} muito mais!")
    elif elefantes in muita_gente:
        print(f"{elefantes} elefantes {incomodam} muita gente")
    
    elefantes += 1

for n in range(1, 11):
    if elefantes == 10:
        print(f"{elefantes} elefantes incomodam muita gente")

    elefantes -= 1

    if elefantes in muito_menos:
        print(f"{elefantes} elefantes {incomodam * elefantes} muito menos!")
    elif elefantes in muita_gente:
        print(f"{elefantes} elefantes {incomodam} muita gente")
    elif elefantes == 1:
        print(f"{elefantes} elefante incomoda muito menos!")
