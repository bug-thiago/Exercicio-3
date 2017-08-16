def Empate(x, y, z):

	nums = [x, y, z]

	nums.sort()

	return nums[2]

try:

	x, y, z = int(input("Digite três valores inteiros: ")), int(input()), int(input())

	print("O maior dos três valores é %d." % Empate(x, y, z))

except:

	print("Não foram digitados valores três inteiros.")