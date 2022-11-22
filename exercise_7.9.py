sandwich_order = ['pastrami', 'bucon', 'pastrami', 'doublecheese', 'meat', 'pastrami']
finished_sandwich = []
print("Sorry pastrami doesn't include your order")
while 'pastrami' in sandwich_order:
    sandwich_order.remove('pastrami')
while sandwich_order:
    order = sandwich_order.pop()
    print(f"I made your {order} sandwich")
    finished_sandwich.append(order)
print(f"Your finished order: ")
for finished_sandwich in finished_sandwich:
    print(f"{finished_sandwich.title()} sadwich")