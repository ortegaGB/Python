CD1,NU1,P1 = input().split(" ") # Atribui os 3 valores e divide-os em espaços.
CD2,NU2,P2 = input().split(" ")
CD1 = int(CD1)
CD2 = int(CD2)
NU1 = int(NU1)
NU2 = int(NU2)
P1 = float(P1)
P2 = float(P2)
VP= (NU1 * P1) + (NU2 * P2)
print("VALOR A PAGAR: R$ %0.2f" %VP)