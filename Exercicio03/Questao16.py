def calendario(m):

	if m == 1:

		return "Janeiro"

	elif m == 2:

		return "Fevereiro"

	elif m == 3:

		return "Março"

	elif m == 4:

		return "Abril"

	elif m == 5:

		return "Maio"

	elif m == 6:

		return "Junho"

	elif m == 7:

		return "Julho"

	elif m == 8:

		return "Agosto"

	elif m == 9:

		return "Setembro"

	elif m == 10:

		return "Outubro"

	elif m == 11:

		return "Novembro"

	elif m == 12:

		return "Dezembro"

	elif m < 1 or m > 12:

		return "O valor não corresponde a nenhum mês."

try:

	m = int(input("Digite um valor inteiro de 1 a 12 correspondente a um mês do calendário gregoriano: "))

	print(calendario(m))

except:

	print("Não foi digitado um valor inteiro.") 