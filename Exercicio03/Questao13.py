def Div(x):

	return x % 2 == 0 and x % 3 == 0

try:

	x = int(input("Digite um valor inteiro: "))

	print(Div(x))

except:

	print("Não foi digitado um valor inteiro.")