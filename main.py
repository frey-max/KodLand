import random
simvols = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
dlina = int(input("Какой длины вы хотите пароль?"))
password = ""
if dlina <= 6:
    print("Слишком короткий пароль...")
else:
    for i in range(dlina):
        password += random.choice(simvols)
    print(password)
