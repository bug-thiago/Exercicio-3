def paridade(x):

	return x % 2 == 0

try:

	x = int(input("Digite um número inteiro: "))

	print(paridade(x))

except:

	print("Não foi digitado um valor inteiro.")