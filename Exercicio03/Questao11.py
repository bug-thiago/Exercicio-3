def Termometro(t):

	if t > 36.5:

		return "Está com febre"

	else:

		return "Sem febre"

try:

	t = float(input("Digite um valor real correspondente à temperatura corporal de uma pessoa: "))

	print(Termometro(t))

except:

	print("Não foi digitado um valor real.")