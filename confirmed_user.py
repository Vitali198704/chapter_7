#начинаем с двух списков: пользователей для проверки
# и пустого списка для хранения проверенных пользователей.
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
#проверяем каждого пользователя, пока остаются непроверенные пользователи. Каждый пользователь, прошедший проверку, перемещается в спиок проверенных.
while unconfirmed_users:
    current_users = unconfirmed_users.pop()
    
    print(f"Verifying user: {current_users.title()}")
    confirmed_users.append(current_users)
#Вывод всех проверенных пользователей.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())