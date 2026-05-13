import random
import string

alfabeto = list(string.ascii_lowercase)
random.shuffle(alfabeto)

letra_sorteada = random.choice(string.ascii_lowercase)
posicao_real = alfabeto.index(letra_sorteada)

print(f"Letra: {letra_sorteada}")
palpite = int(input("Posição (1-26): "))

if palpite-1 == posicao_real:
    print("Acertou")
else:
    print(f"Errou. Era {posicao_real+1}")