def multi(x):

	return x % 5 == 0

try:

	x = int(input("Digite um valor inteiro: "))

	print(multi(x))

except:

	print("Não foi digitado um valor inteiro.")