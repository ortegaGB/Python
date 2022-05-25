'''\
1012, Área
Make a program that reads three floating point values: A, B and C. Then, calculate and show:
a) the area of the rectangled triangle that has base A and height C.
b) the area of the radius's circle C. (pi = 3.14159)
c) the area of the trapezium which has A and B by base, and C by height.
d) the area of the square that has side B.
e) the area of the rectangle that has sides A and B.
'''
variables = input().split(" ")
a,b,c = variables
rt= float(a) * float(c) / 2
ac= 3.14159 * float(c) ** 2
tp= (float(a)+float(b))* float(c) / 2
sq= float(b)**2
rc= float(a)*float(b)
print("TRIANGULO: %0.3f\nCIRCULO: %0.3f\nTRAPEZIO: %0.3f\nQUADRADO: %0.3f\nRETANGULO: %0.3f"%(rt,ac,tp,sq,rc))