def tratamento(nome, sexo):

	if sexo.lower() == "masculino":

		return "\nIlmo. Sr. %s [...]" % nome

	elif sexo.lower() == "feminino":

		return "\nIlmo. Sra. %s [...]" % nome

	else:

		return "O sexo não pôde ser identificado."

nome, sexo = input("Nome: "), input("Sexo: ")

print(tratamento(nome, sexo))