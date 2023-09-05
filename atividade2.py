"""
Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo,
o mais gordo e o mais magro, para isto você deve fazer um programa que pergunte a cada um dos clientes
da academia seu código, sua altura e seu peso. O final da digitação de dados deve ser dada quando
o usuário digitar 0 (zero) no campo código. Ao encerrar o programa também deve ser informados
os códigos e valores do clente mais alto, do mais baixo, do mais gordo e do mais magro,
além da média das alturas e dos pesos dos clientes.

Versão: 1.0
"""

codigos = []
alturas = []
pesos = []

while True:
    codigo = input("Digite o código do cliente (ou 0 para sair): ")
    if codigo == '0':
        break

    altura = float(input("Digite a altura do cliente em metros (separado por ponto): "))
    peso = float(input("Digite o peso do cliente em kg (separado por ponto): "))

    codigos.append(codigo)
    alturas.append(altura)
    pesos.append(peso)

if len(codigos) > 0:
    indice_mais_alto = alturas.index(max(alturas))
    indice_mais_baixo = alturas.index(min(alturas))
    indice_mais_gordo = pesos.index(max(pesos))
    indice_mais_magro = pesos.index(min(pesos))

    print("\nRelatório:")
    print(f"Mais alto - Código: {codigos[indice_mais_alto]}, Altura: {alturas[indice_mais_alto]}")
    print(f"Mais baixo - Código: {codigos[indice_mais_baixo]}, Altura: {alturas[indice_mais_baixo]}")
    print(f"Mais gordo - Código: {codigos[indice_mais_gordo]}, Peso: {pesos[indice_mais_gordo]}")
    print(f"Mais magro - Código: {codigos[indice_mais_magro]}, Peso: {pesos[indice_mais_magro]}")

    media_alturas = sum(alturas) / len(alturas)
    media_pesos = sum(pesos) / len(pesos)

    print(f"Média das alturas: {media_alturas:.2f}")
    print(f"Média dos pesos: {media_pesos:.2f}")
else:
    print("Nenhum cliente cadastrado.")
