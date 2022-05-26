num_jogadores = int(input())
ts_saque = 0
tt_saque = 0
ts_block = 0
tt_block = 0
ts_atack = 0
tt_atack = 0

for i in range(num_jogadores):
    nome_jogador = input()
    saque,bloqueio,ataque = map(int,input().split())
    s_saque,s_bloqueio,s_ataque = map(int,input().split())
    ts_saque += s_saque
    tt_saque += saque
    ts_block += s_bloqueio
    tt_block += bloqueio
    ts_atack += s_ataque
    tt_atack += ataque
per_saque = (ts_saque / tt_saque) * 100
per_block = (ts_block / tt_block) * 100
per_atack = (ts_atack / tt_atack) * 100
print("Pontos de Saque: %.2f" %per_saque,"%.")
print("Pontos de Bloqueio: %.2f" %per_block,"%.")
print("Pontos de Ataque: %.2f" %per_atack,"%.")