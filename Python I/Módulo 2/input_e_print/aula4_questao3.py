#3) Você está desenvolvendo um programa para calcular o preço total de uma compra em uma loja online. O preço dos produtos
#é calculado multiplicando a quantidade pelo preço unitário. Escreva um programa em Python que solicite do usuário o nome,
#o preço unitário e a quantidade de 3 produtos comprados e imprima ao final o preço total da compra. Note no exemplo a 
#seguir que:
#Cada entrada de dados tem uma mensagem indicando o dado solicitado (mensagens em itálico, dado de entrada em negrito).
#A saída deve estar formatada exatamente como indicado (a string "Total: R$" e o preço com um separador de milhar e duas 
#casas decimais).
#Entrada:
#Digite o nome do produto 1: calça
#Digite o preço unitário do produto 1: 199.90
#Digite a quantidade do produto 1: 3
#Digite o nome do produto 2: camisa
#Digite o preço unitário do produto 2: 49.95
#Digite a quantidade do produto 2: 10
#Digite o nome do produto 3: cinto
#Digite o preço unitário do produto 3: 25
#Digite a quantidade do produto 3: 3
#Saída:
#Total: R$1,174.20
produto1 = input("Digite o nome do produto 1: ")
preço_produto1 = float(input(("Digite o preço unitário do produto 1: ")))
quantidade_produto1 = int(input("Digite a quantidade do produto 1: "))

produto2 = input("Digite o nome do produto 2: ")
preço_produto2 = float(input(("Digite o preço unitário do produto 2: ")))
quantidade_produto2 = int(input("Digite a quantidade do produto 2: "))

produto3 = input("Digite o nome do produto 3: ")
preço_produto3 = float(input(("Digite o preço unitário do produto 3: ")))
quantidade_produto3 = int(input("Digite a quantidade do produto 3: "))

produto1_valor = (preço_produto1 * quantidade_produto1)
produto2_valor = (preço_produto2 * quantidade_produto2)
produto3_valor = (preço_produto3 * quantidade_produto3)

print(f"{produto1} = {produto1_valor}")
print(f"{produto2} = {produto2_valor}")
print(f"{produto3} = {produto3_valor}")

preço_total = (preço_produto1 * quantidade_produto1) + (preço_produto2 * quantidade_produto2) + (preço_produto3 * quantidade_produto3)
print(f"Preço total = R${preço_total}")

