n = int(input())
fatorial = 1
for i in range(n):
    fatorial = fatorial * n
    n -= 1
print(fatorial)