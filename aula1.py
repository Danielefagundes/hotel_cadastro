print("Bem vindo à Nova hotel")
print('Vamos começar seu cadastro')

#cadastro1

nome1 = input("Digite seu nome: ")
age1 = int(input("Digite sua idade: "))

nome2 = input("Digite seu nome: ")
age2 = int(input("Digite sua idade: "))

nome3 = input("Digite seu nome: ")
age3 = int(input("Digite sua idade: "))


#escolha um quarto

quartos = ["Simples", "Duplo", "Luxo"]
precos = [100, 150, 250]

print("Escolha o tipo de quarto para cada cliente:")
print("1 - Simples")
print("2 - Duplo")
print("3 - Luxo")

#escolher tipo de quarto
cliente_nome1 = int(input("Qual o tipo de quarto para o cliente, " + nome1 + " " +"?: "))
cliente_nome2 = int(input("Qual o tipo de quarto para o cliente, " + nome2 + " " +"?: "))
cliente_nome3 = int(input("Qual o tipo de quarto para o cliente, " + nome3 + " " +"?: "))

#escolher quantos dias
dias_nome1 = int(input("Quantos dias o cliente, " + nome1 + " " +"ficará ?"))
dias_nome2 = int(input("Quantos dias o cliente, " + nome2 + " " +" ficará ?"))
dias_nome3 = int(input("Quantos dias o cliente, " + nome3 + " " +" ficará ?"))

#multiplicar tipo de quarto pelo dias
valor_nome1 = precos[cliente_nome1] * dias_nome1
valor_nome2 = precos[cliente_nome2] * dias_nome2
valor_nome3 = precos[cliente_nome3] * dias_nome3

print(f"O valor total para o quarto de {nome1}, será o valor de {valor_nome1} R$.")
print(f"O valor total para o quarto de {nome2}, será o valor de {valor_nome2} R$.")
print(f"O valor total para o quarto de {nome3}, será o valor de {valor_nome3} R$.")