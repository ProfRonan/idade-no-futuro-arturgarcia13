yearNow = int(input("Digite o ano atual: "))
ageNow = int(input("Digite sua idade atual: "))
yearFuture = int(input("Digite um ano no futuro: "))
name = input("Digite seu nome: ")
ageFuture = (yearFuture - yearNow ) + ageNow

print(f"{name}, no ano de {yearFuture} você terá {ageFuture} anos ")
