# 1) Escreva um programa que lê dois números e informa se a sua soma é par ou ímpar. Critério: se o resto da divisão do 
# número por 2 for 0, o número é par, caso contrário é ímpar. Lembre-se do operador do python % que retorna o resto de 
# uma divisão.

numero_um = int(input("Digite o primeiro número: "))
numero_dois = int(input("Digite o segundo número: "))

soma = numero_um + numero_dois

if  soma % 2 == 0:
    print("Par")
else:  
    print("Ímpar")