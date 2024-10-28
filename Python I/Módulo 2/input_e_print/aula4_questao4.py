#4) Escreva um programa que leia um valor inteiro referente a uma quantia em reais e calcule a menor quantidade possível 
#de notas necessárias para pagar aquele valor. As notas possíveis são: 100, 50, 20, 10, 5, 2, 1. A saída deve estar 
#formatada exatamente como indicado. 
#Entrada: 576
#Saída:
#5 nota(s) de R$100,00
#1 nota(s) de R$50,00
#1 nota(s) de R$20,00
#0 nota(s) de R$10,00
#1 nota(s) de R$5,00
#0 nota(s) de R$2,00
#1 nota(s) de R$1,00

valor = int(input("Digite o valor: "))

notas_100 = valor//100 
notas_100 = valor % 100

notas_50 = valor//50 
notas_50 % 50

notas_20 = valor//20 
notas_20 % 20

notas_10 = valor//10
notas_10 % 10

notas_5 = valor//5
notas_5 % 5

notas_2 = valor//2 
notas_2 % 2

notas_1 = valor//1 
notas_1 % 1

print(f"{notas_100} nota(s) de 100")
print(f"{notas_50}nota(s) de 50")
print(f"{notas_20} nota(s) de 20")
print(f"{notas_10} nota(s) de 10")
print(f"{notas_5} nota(s) de 5")
print(f"{notas_2} nota(s) de 2")
print(f"{notas_1} nota(s) de 1")