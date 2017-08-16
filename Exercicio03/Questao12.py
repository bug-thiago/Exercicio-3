def multi(x):

	if x % 7 == 0:

		return "O número é múltiplo de 7"

	else:

		return "O número não é múltiplo de 7"

try:

	x = int(input("Digite um valor inteiro: "))

	print(multi(x))

except:

	print("Não foi fornecido um valor inteiro.")