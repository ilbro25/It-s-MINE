import random
sym = "abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890.,/_-=+?!@#$%^&*()"
while (True):
    leight = int(input("Введите желаемую длину пароля: "))
    password = ""
    for i in range(leight):
        password += random.choice(sym)
    print(password)
