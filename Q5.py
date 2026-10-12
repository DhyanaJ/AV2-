def filtrar_alunos(notas):
    aprovados= []

    for nota in notas:
        if nota >=7:
            aprovados.append(nota)

    return aprovados

notas = []

for i in range (3): 
    nota = float(input("Digite uma nota: "))
    notas.append(nota)

total = filtrar_alunos(notas)

print("Notas dos aprovados", total)