def Par_Impa(x, y):

	if x % 2 == 0 and y % 2 == 0:

		return "Os dois são pares"

	elif x % 2 != 0 and y % 2 != 0:

		return "Os dois são ímpares"

	elif x % 2 == 0 and y % 2 != 0:

		return "O primeiro é par e o segundo é ímpar"

	elif x % 2 != 0 and y % 2 == 0:

		return "O primeiro é ímpar e o segundo é par"

try:

	x, y = int(input("Digite dois números inteiros: ")), int(input())

	print(Par_Impa(x, y))

except:

	print("Não foram digitados valores inteiros.")