def Semaforo(cor):

	if cor == "V":

		return "Siga"

	elif cor == "A":

		return "Atenção"

	elif cor == "E":

		return "Pare"

cor = input("Digite a letra correspondente à atual cor do semáforo (use 'V' para verde, 'A' para amarelo e 'E' para vermelho): ")

if semaforo(cor) == None:

	print("O caractere Digitado não corresponde a nenhuma cor. Tente novamente.")

else:

	print(Semaforo(cor))
