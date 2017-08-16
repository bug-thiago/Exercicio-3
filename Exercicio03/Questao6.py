def Cin(x):

	if x > 20:

		return "Vá ao cinema"

	else:

		return "Fique em casa vendo TV"

try:

	x = float(input("Quanto dinheiro você tem (em R$): "))

	print(Cin(x))

except:

	print("Não foi digitado um valor real.")