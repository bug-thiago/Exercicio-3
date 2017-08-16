def maior(x, y):

	if x > y:

		return x

	else:

		return y

try:

	x, y = float(input("Digite dois números reais: ")), float(input())

	if x != y:

		print("O maior valor é %f.\n" % maior(x, y))

	else:

		print("Os valores são iguais.")

except:

	print("Não foram Digitados valores reais.")