"""
Este exercício busca ler um inteiro que representa a idade em dias, imprindo-a em anos, meses e dias
"""
idade_dias = int(input())

#Anos, com a divisão inteira representando o valor que fica e em módulo o valor "que vai".
idade_anos = idade_dias // 365
idade_resto = idade_dias % 365

#Meses
idade_meses = idade_resto // 30
idade_resto = idade_resto % 30

#Dias
dias_finais = idade_resto

print("%i ano(s)" %idade_anos)
print("%i mes(es)" %idade_meses)
print("%i dia(s)" %dias_finais)
