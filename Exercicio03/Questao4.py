def sort(x, y, z):

	nums = [x, y, z]

	nums.sort()

	print("Em ordem crescente: %f, %f, %f." % (nums[0], nums[1], nums[2])).rstrip('.').rstrip('0')

try:

	x, y, z = float(input("Digite três números: ")), float(input()), float(input())

	sort(x, y, z)

except:

	print("Não foram digitados valores reais.")