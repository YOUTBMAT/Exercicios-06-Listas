import random
import string

alfabeto = list(string.ascii_lowercase)
random.shuffle(alfabeto)

letraSorteada = random.choice(string.ascii_lowercase)
posicaoReal = alfabeto.index(letraSorteada)

print(f"Letra: {letraSorteada}")
palpite = int(input("Posição (1-26): "))

if palpite-1 == posicaoReal:
    print("Acertou")
else:
    print(f"Errou. Era {posicaoReal+1}")