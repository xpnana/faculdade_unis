"""
Exercício 4: Verificador de Números Primos (1 a 100).

Enunciado:
    Implementar uma função que retorne verdadeiro se o número for primo
    (falso caso contrário). Testar de 1 a 100.
"""

def retornar_primo(n):
    if n <= 1:
        return False
    #
    for i in range (2, n):
        if n % i == 0:
            return False
    #
    return True

for x in range (1,101):
    print(f"{x} {retornar_primo(x)}")
