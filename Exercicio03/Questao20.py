def imc(massa, altura):

	return massa / (altura ** 2)

massa, altura = float(input("Digite os valores reais correspondentes, respectivamente, à massa (em kg) e à altura (em m): ")), float(input())

if massa > 0 and altura > 0:

	imc = imc(massa, altura)

	if imc < 18.5:

		classificacao = "Abaixo do peso"

	elif imc < 25 and imc >= 18.5:

		classificacao = "Peso normal"

	elif imc < 30 and imc >= 25:

		classificacao = "Sobrepeso"

	elif imc < 35 and imc >= 30:

		classificacao = "Obeso leve"

	elif imc < 40 and imc >= 35:

		classificacao = "Obeso moderado"

	elif imc >= 40:

		classificacao = "Obeso mórbido"

	print("IMC = %.3f" % imc)
	print("%s" % classificacao)

else:

	print("Valor(es) inválido(s). Tente novamente.")