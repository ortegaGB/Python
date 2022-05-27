partidas_jogadas = int(input())

for i in range(partidas_jogadas):
    jogada_1 = input()
    jogada_2 = input()
    if jogada_1 == jogada_2 == "pedra":
        print("Sem ganhador")
    elif jogada_1 == jogada_2 == "papel":
        print("Ambos venceram")
    elif jogada_1 == jogada_2 == "ataque":
        print("Aniquilacao mutua")
    #Casos onde o jogador 1 vence
    elif jogada_1 == "ataque" and jogada_2 != "ataque":
        print("Jogador 1 venceu")
    elif jogada_1 == "pedra" and jogada_2 == "papel" and jogada_2 != "ataque":
        print("Jogador 1 venceu")
    else:
        print("Jogador 2 venceu")