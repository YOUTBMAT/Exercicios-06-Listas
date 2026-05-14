tabuleiro = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
venceu = False

for rodada in range(9):
    print(f"\n{tabuleiro[0]}|{tabuleiro[1]}|{tabuleiro[2]}")
    print(f"{tabuleiro[3]}|{tabuleiro[4]}|{tabuleiro[5]}")
    print(f"{tabuleiro[6]}|{tabuleiro[7]}|{tabuleiro[8]}")
    
    jogador = "X" if rodada % 2 == 0 else "O"
    posicao = int(input(f"Jogador {jogador}: "))
    tabuleiro[posicao] = jogador

    # Combinacoes de vitoria (indices da lista)
    v = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    
    for a, b, c in v:
        if tabuleiro[a] == tabuleiro[b] == tabuleiro[c]:
            print(f"\nJogador {jogador} VENCEU!")
            venceu = True
            break
    
    if venceu: break
else:
    print("\nEMPATE!")