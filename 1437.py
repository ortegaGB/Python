#N,L,S,O = 0,1,2,3
num_comandos = int(input())

while num_comandos != 0:
    final_dir = 1
    comandos = input()
    for i in range(num_comandos):
        if comandos[i] == "D":
            final_dir += 1
        else:
            final_dir -= 1
    final_dir = (final_dir) % 4
    if final_dir == 1:
        print("N")
    elif final_dir == 2:
        print("L")
    elif final_dir == 3:
        print("S")
    else:
        print("O")
    num_comandos = int(input())