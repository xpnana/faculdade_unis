"""
Exercício 2: Verificador e Calculador de Área de Triângulos.

Enunciado:
    Elaborar um programa que lê 3 valores a, b, c e verifica se eles formam ou
    não um triângulo. Supor que os valores lidos são inteiros e positivos.
    Caso os valores formem um triângulo, calcular e escrever a área deste triângulo.
    Se não formam triângulo escrever os valores lidos.
    (Regra: Se a > b + c não formam triângulo algum, se a é o maior).
"""

a = float(input('Digite um valor: '))
b = float(input('Digite outro valor: '))
c = float(input('Digite o último valor: '))

if (a + b > c) and (a + c > b)  and (b +c > a):
    #1 semiperimetro (s)
    s = (a + b + c) / 2
    area_triangulo = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    print(f"Os valores formam um triângulo! A área é: {area_triangulo:.2f}")
else:
    print(f"Os valores lidos não formam um triângulo: a = {a}, b = {b}, c = {c}")
