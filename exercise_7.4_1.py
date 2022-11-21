requested_topping = ("\nIf you order is finished, please, input 'quit'")
requested_topping += "\n\nPlease choose your topping for pizza: "
active = True
while active:
    topping = input(requested_topping)
    if topping == 'quit':
        active = False
    else:
        print(f"\n{topping} is add in your order")