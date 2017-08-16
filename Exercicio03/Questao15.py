def Vogal(l):

	return l == "a" or l == "e" or l == "i" or l == "o" or l == "u"

l = input("Digite uma letra: ")

if len(l) == 1:

	print(Vogal(l))

else:

	print("Somente uma letra deve ser fornecida.")