sandwich_order = ['bucon', 'doublecheese', 'meat']
finished_sandwich = []
while sandwich_order:
    order = sandwich_order.pop()
    print(f"I made your {order} sandwich")
    finished_sandwich.append(order)
print(f"Your finished order: ")
for finished_sandwich in finished_sandwich:
    print(f"{finished_sandwich.title()} sadwich")