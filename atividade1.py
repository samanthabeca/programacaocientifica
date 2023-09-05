"""
Faça um Programa que peça os 3 lados de um triângulo.
O programa deverá informar se os valores podem ser um triângulo.
Indique, caso os lados formem um triângulo, se o mesmo é: equilátero (todos os lados iguais),
isósceles (dois lados iguais) ou escaleno (todos medidas diferentes).
Exibindo o tamanho de cada lado e o tipo de triângulo formatado pelo f_string

Autora: Samantha Beca
Versão: 2.0.0
"""

lado1 = float(input("Entre com o 1º lado: ")) 
lado2 = float(input("Entre com o 2º lado: "))
lado3 = float(input("Entre com o 3º lado: "))
if lado1 == lado2 and lado1 == lado3:
    print("Equilátero. Três lados iguais.")
    print("=========================================")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("Isósceles. Dois lados iguais.")
    print("=========================================")
else:
    print("Escaleno. Três lados diferentes.")
    print("=========================================")
print("Lado 1: " + f'{lado1}' + " || Lado 2: " + f'{lado2}' + " || Lado 3: " + f'{lado3}')
