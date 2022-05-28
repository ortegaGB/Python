n = int(input())
denominador = 1

for i in range(n):
    if n % denominador == 0:
        print(denominador)
        denominador += 1
    else:
        denominador += 1