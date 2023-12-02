# Add 1 to each digit of a number

br = int(input("Input a number: "))
nbr = 0
des = 0
while br > 0:
	nbr = nbr + ((br % 10)+1)*10**des
	br = br // 10
	des += 1
print("New number: ", nbr)

