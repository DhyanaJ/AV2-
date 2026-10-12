def calcular_media(notas):
    media = sum(notas) / len(notas)
    return media

notas = []

for i in range(3):
    nota = float(input("Digite uma nota: "))
    notas.append(nota)

total = calcular_media(notas)

print(f"Média:{total: .2f}")