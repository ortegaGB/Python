A,B,C = map(float,input().split())

perimetro = A + B + C
area = ((A + B) * C) / 2

if A > (B - C) and A < B + C:
    print("Perimetro = %.1f" % perimetro)
else:
    print("Area = %.1f" % area)