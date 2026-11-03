"""
Exercício 3: Localizador do Menor Número Inteiro.

Enunciado:
    Faça um programa que leia 3 números inteiros e mostre o menor deles.
"""

num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite  segundo valor: '))
num3 = int(input('Digite o terceiro valor: '))

if num1 <= num2 and num1 <= num3:
    menor = num1
elif num2 <= num1 and num2 <= num3:
    menor = num2
else: menor = num3

print(f"O menor valor é: {menor}")