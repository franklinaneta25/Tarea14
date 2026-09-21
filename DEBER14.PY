def calcular_promedio(nota1, nota2, nota3):
    suma = nota1 + nota2 + nota3
    promedio = suma / 3
    return promedio

n1 = 8.5
n2 = 9.0
n3 = 7.5

promedio_final = calcular_promedio(n1, n2, n3)
print("el promedio final es:", promedio_final)