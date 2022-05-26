numero_rodadas = int(input())
teste = 0

while numero_rodadas != 0:
    teste += 1
    jogador_1 = input()
    jogador_2 = input()
    print("Teste", teste)
    for i in range(numero_rodadas):
        j1,j2 = map(int,input().split())
        if (j1 + j2) % 2 == 0:
            print(jogador_1)
        else:
            print(jogador_2)
    print()
    numero_rodadas = int(input())