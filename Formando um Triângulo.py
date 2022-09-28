# Descrição: verificar se as medidas dos três números formam um triângulo.
# Autor: Diego Vale do Nascimento - 18/09/2022

n1 = float(input("Digite o primeiro número inteiro: "))
n2 = float(input("Digite o segundo número inteiro: "))
n3 = float(input("Digite o terceiro número inteiro: "))
print("=================================")
if (n1 + n2 < n3) or (n1 + n3 < n2) or (n2 + n3 < n1):
    print('Nao é um triangulo')
elif (n1 == n2) and (n1 == n3):
    print('Triângulo Equilátero')
elif (n1==n2) or (n1==n3) or (n2==n3):
    print('Triângulo Isósceles')
else:
    print('Triângulo Retângulo')