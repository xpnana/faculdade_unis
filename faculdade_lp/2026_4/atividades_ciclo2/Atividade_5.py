"""
Exercício 5: Inversor de Letras por Palavra.

Enunciado:
    Escreva uma função que:
    a) Receba uma frase como parâmetro.
    b) Retorne uma nova frase com cada palavra com as letras invertidas.
"""

def frase_invertida(n):
    nova_frase = ""

    for i in range (len(n) - 1, -1, -1):
        nova_frase += n[i]

    print(nova_frase)

frase_usuario = input("Digite uma frase para inverter: ")

frase_invertida(frase_usuario)