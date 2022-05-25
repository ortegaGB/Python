N = int(input())
fib1 = 1
fib2 = 1
cont = 1
myString = "0"
while cont < N:
    myString += " " + str(fib1)
    soma = fib1 + fib2
    fib1 = fib2
    fib2 = soma
    cont = cont + 1
print(myString)