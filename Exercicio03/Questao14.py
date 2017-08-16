def Votar(ano):

	if 2018 - ano >= 16:

		return "Tu poderás votar"

	else:

		return "Tu não poderás votar"

try:

	a = int(input("Digite o valor correspondente ao teu ano de nascimento: "))

	print(Votar(a))

except:

	print("Não foi digitado um valor inteiro.")