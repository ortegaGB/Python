"""
Este exercício procura decompor em notas e moedas valores decimais, dispondo a quantidade de cédulas e moedas
para decompor o valor de entrada.
"""
valor_inicial = float(input())

#Conversão do valor em decimal para um inteiro por completo
valor_inicial = valor_inicial * 100

#Notas de 100, note que, o valor será dividido por mais dois zeros em compensação com o a conversão acima, queremos só os inteiros.
notas100 = valor_inicial // 10000
valor_resto = valor_inicial % 10000
"""
A divisão inteira permite extrair o valor de notas, o "módulo" extrai a quantia que passa a próxima "casa" da decomposição.
"""

#Notas de 50, a divisão por dois zeros mantem-se.
notas50 = valor_resto // 5000
valor_resto = valor_resto % 5000

#Notas de 20.
notas20 = valor_resto // 2000
valor_resto = valor_resto % 2000

#Notas de 10.
notas10 = valor_resto // 1000
valor_resto = valor_resto % 1000

#Notas de 5.
notas5 = valor_resto // 500
valor_resto = valor_resto % 500

#Notas de 2.
notas2 = valor_resto // 200
valor_resto = valor_resto % 200


#Com moedas de 1
m1 = valor_resto // 100
valor_resto = valor_resto % 100

#Com moedas de 50 cent.
m05 = valor_resto // 50
valor_resto = valor_resto % 50

#Com moedas de 25 cent.
m25 = valor_resto // 25
valor_resto = valor_resto % 25

#Com moedas de 10 cent.
m10 = valor_resto // 10
valor_resto = valor_resto % 10

#Com moedas de 5 cent.
m5 = valor_resto // 5
valor_resto = valor_resto % 5

#Com moedas de 1 cent.
m01 = valor_resto // 1

print(("NOTAS:\n"+
      "%i nota(s) de R$ 100.00\n"+
      "%i nota(s) de R$ 50.00\n"+
      "%i nota(s) de R$ 20.00\n"+
      "%i nota(s) de R$ 10.00\n"+
      "%i nota(s) de R$ 5.00\n"+
      "%i nota(s) de R$ 2.00\n"
      "MOEDAS:\n"+
      "%i moeda(s) de R$ 1.00\n"+
      "%i moeda(s) de R$ 0.50\n"+
      "%i moeda(s) de R$ 0.25\n"+
      "%i moeda(s) de R$ 0.10\n"+
      "%i moeda(s) de R$ 0.05\n"+
      "%i moeda(s) de R$ 0.01") %(notas100,notas50,notas20,notas10,notas5,notas2,m1,m05,m25,m10,m5,m01))