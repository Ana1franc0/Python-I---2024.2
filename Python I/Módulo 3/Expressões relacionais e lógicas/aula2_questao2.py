#2) Dando continuidade à questão anterior, um outro bar permite a entrada de grupos onde pelo menos uma pessoa é maior 
#de idade (ficando responsável pelas outras). Ajuste sua resposta da questão anterior, ainda solicitando as idades de 
#Juliana e Cris, mas ajustando a expressão para esse novo cenário, imprimindo True se puderem entrar no bar, e False 
#caso contrário.

Juliana = int(input("Digite idade de Juliana: "))
Cris = int(input("Digite idade de Cris: "))

if Juliana >=18 or Cris >=18:
    print(True)
else:
    print(False)