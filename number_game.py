import random
import numbers
contador=0
print("Gerando um numero aleatorio de 1 a 10...")
num = random.randint(1,10)
if num== 1 or num ==2 or num ==3 or num ==4 or num ==5:
    print (" o numero gerado é um número baixo")
elif num ==6 or num ==7 or num ==8 or num ==9 or num == 10:
    print("o numero gerado é um número alto")
quest=input("Tente adivinhar o número entre 1 a 10: ")
while num != quest:
    print("Número errado")
    print("Deseja tentar novamente?")
    print("[s/n]")
    repeat=input()
    if repeat == 's':
        quest=input("Tente adivinhar o número entre 1 a 10: ")
    elif repeat== 'n':
        print("programa encerrado")
        break
if num == quest:
    print("número adivinhado corretamente.")

