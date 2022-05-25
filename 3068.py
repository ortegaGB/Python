x1,y1,x2,y2 = map(int,input().split(" "))
cont = 1
num_final = 0
while not x1 == y1 == x2 == y2 == 0:
    num_met = int(input())

    for i in range (num_met):
    
        mx,my = map(int,input().split(" "))

        if x1 <= mx <= x2 and y2 <= my <= y1:
            num_final += 1
    print("Teste",cont)
    cont += 1
    print(num_final)
    num_final = 0 
    x1,y1,x2,y2 = map(int,input().split(" "))