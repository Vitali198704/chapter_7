requested_topping = ("\nIf you order is finished, please, input 'quit'")
requested_topping += "\n\nPlease choose your topping for pizza: "
while True:
    topping = input(requested_topping)
    if topping == 'quit':
        break
    else:
        print(f"\n{topping} is add in your order")