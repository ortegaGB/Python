palavra_um  = input()
palavra_dois = input()
palavra_tres = input()

if palavra_um == "vertebrado":
    if palavra_dois == "ave":
        if palavra_tres == "carnivoro":
            print("aguia")
        else:
            print("pomba")
    if palavra_dois == "mamifero":
        if palavra_tres == "onivoro":
            print("homem")
        else:
            print("vaca")
if palavra_um == "invertebrado":
    if palavra_dois == "inseto":
        if palavra_tres == "hematofago":
            print("pulga")
        else:
            print("lagarta")
    if palavra_dois == "anelideo":
        if palavra_tres == "hematofago":
            print("sanguessuga")
        else:
            print("minhoca")