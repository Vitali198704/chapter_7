age = input("\nPlease, enter you age: ")
age = int(age)
while True:
	message = input(age)
	if age <= 3:
		price = 0
	elif age <= 18:
		price = 25
	else:
		price = 20
	print(f"Your admission cost is ${price}.")
	break
