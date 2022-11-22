countries = {}
active = True
while active:
    name = input("\nWhat is your name? ")
    country = input("Which country would you like to visit? ")
    countries[name] = country
    repeat = input("Would you like to let another person respond? (yes/no)")
    if repeat == 'no':
        active = False
print("\n---Poll Result---")
for name, country in countries.items():
    print(f"{name.title()} would like to visit {country.title()}.")