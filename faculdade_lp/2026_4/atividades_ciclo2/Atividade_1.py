"""
Exercício 1: Conversão de Idade de Dias para Anos, Meses e Dias.

Enunciado:
    Faça um programa que leia a idade de uma pessoa expressa em dias e
    mostre-a expressa em anos, meses e dias.
"""

idade = int(input('Digite sua idade em dias: '))

calculo_anos = idade // 365
resto_anos = idade % 365

calculo_meses = resto_anos // 30
resto_meses = resto_anos % 30


txt_ano = "ano" if calculo_anos == 1 else "anos"
txt_mes = "mês" if calculo_meses == 1 else "meses"
txt_dia = "dia" if resto_meses == 1 else "dias"

resultado_final = f"{calculo_anos} {txt_ano}, {calculo_meses} {txt_mes}, {resto_meses} {txt_dia}."

print(resultado_final)
