import random
import string

print("===== PASSWORD GENERATOR =====")

length = int(input("Enter password length: "))

if length < 4:
    print("Password length must be at least 4!")

else:
    characters = string.ascii_letters + string.digits + string.punctuation
    
    password = ''.join(random.choice(characters) for i in range(length))

    print("\nGenerated Password:", password)

    print("Password Generated Successfully!")