x,y,z = input().split(" ")
x,y,z = float(x), float(y), float(z)

valores = [x,y,z]
valores.sort(reverse=True)
A,B,C = valores[0],valores[1],valores[2]

if A >= B + C:
    print("NAO FORMA TRIANGULO")
elif (A**2) == (B**2) + (C**2):
    print("TRIANGULO RETANGULO")
    if A == B and B == C and A == C:
        print("TRIANGULO EQUILATERO")
    if A != B and B == C and C != A:
        print("TRIANGULO ISOSCELES")
    if B != A and C == A and B != C:
        print("TRIANGULO ISOSCELES")
    if C != A and B == A and C != B:
        print("TRIANGULO ISOSCELES")
elif A**2 > B**2 + C**2:
    print("TRIANGULO OBTUSANGULO")
    if A == B and B == C and A == C:
        print("TRIANGULO EQUILATERO")
    if A != B and B == C and C != A:
        print("TRIANGULO ISOSCELES")
    if B != A and C == A and B != C:
        print("TRIANGULO ISOSCELES")
    if C != A and B == A and C != B:
        print("TRIANGULO ISOSCELES")
elif A**2 < B**2 + C**2:
    print("TRIANGULO ACUTANGULO")
    if A == B and B == C and A == C:
        print("TRIANGULO EQUILATERO")
    if A != B and B == C and C != A:
        print("TRIANGULO ISOSCELES")
    if B != A and C == A and B != C:
        print("TRIANGULO ISOSCELES")
    if C != A and B == A and C != B:
        print("TRIANGULO ISOSCELES")