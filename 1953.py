while True:
    try:
        num_alunos = int(input())

        num_epr = 0
        num_ehd = 0
        num_int = 0

        for i in range(num_alunos):
            n_chamada,curso = input().split()
            if curso == "EPR":
                num_epr += 1
            elif curso == "EHD":
                num_ehd += 1
            else:
                num_int += 1
        print("EPR:", num_epr)
        print("EHD:", num_ehd)
        print("INTRUSOS:", num_int)
    except EOFError:
        break