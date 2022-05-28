num_comp,qnt_papl,qnt_nece = map(int,input().split())

if num_comp * qnt_nece >= qnt_papl:
    print("N")
else:
    print("S")