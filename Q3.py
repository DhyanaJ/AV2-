def carga_horaria(horas):
    if horas >= 40:
        return "Carga horária completa"
    else:
        return "Carga horária incompleta"


horas = float (input("Digite as horas trabalhadas: "))

resultado = carga_horaria(horas)               

print(resultado)