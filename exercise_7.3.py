number = input("Enter a number, please: ")
number = int(number)

if number % 10 ==0:
	print(f"\nThe number {number} is aliquot.")
else:
	print(f"\nThe number {number} is not aliquot.")