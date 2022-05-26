a, b, c = map(int,input().split())

if a > b - c and b > a - c and c > a - b:
    triangleType = ""
    if a == b == c:
        triangleType = "Equilatero"
    elif a == b != c or b != c == a or c != b == a:
        triangleType = "Isoceles"
    else:
        triangleType = "Escaleno"
    rectangleType = ""
    if (a ** 2) == (b**2) + (c**2) or (b**2) == (a**2) + (c**2) or (c**2) == (b**2) + (a**2):
        rectangleType = "S"
    else:
        rectangleType = "N"
    print("Valido-%s" %triangleType)
    print("Retangulo:", rectangleType)
else:
    print("Invalido")