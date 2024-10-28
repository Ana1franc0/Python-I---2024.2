#1) Juliana e Cris querem entrar em um bar, mas só podem se ambos forem maiores de idade (>17). Escreva um programa que 
# solicite as idades de Juliana e Cris e imprima True se ambas forem maiores de 17 anos, indicando que podem entrar no 
# bar, e False caso contrário.

Juliana = int(input("Digite idade de Juliana: "))
Cris = int(input("Digite idade de Cris: "))

if Juliana >=18 and Cris >=18:
    print(True)
else:
    print(False)