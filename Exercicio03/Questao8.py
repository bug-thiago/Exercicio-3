def Neg_Pos(x):

	if x == 0:

		return "igual a zero"

	elif x < 0:

		return "negativo"

	elif x > 0:

		return "positivo"

try:

	x = int(input("Digite um valor inteiro: "))

	print("O número %d é %s." % (x, Neg_Pos(x)))

except:

	print("Não foi digitado um valor inteiro.")