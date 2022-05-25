n1, n2 , n3 , n4 = map(float, input().split())
media = ((n1 * 2) + (n2 * 3) + (n3 * 4) + (n4 * 1)) / 10
print("Media: %.1f" %media)
if media >= 7.0:
    print("Aluno aprovado.")
elif media < 5.0:
    print("Aluno reprovado.")
elif 5.0 <= media <= 6.9:
    print("Aluno em exame.")
    exame = float(input())
    media_final = (exame + media) / 2
    if exame >= 5.0:
        print("Nota do exame: %.1f" %(exame))
        print("Aluno aprovado.")
        print("Media final: %.1f" %(media_final))
    if exame < 5.0:
        print("Nota do exame: %.1f" %(exame))
        print("Aluno reprovado.")
        print("Media final: %.1f" %(media_final))