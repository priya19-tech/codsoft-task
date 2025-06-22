import random
import string

def generate_password():
    print(" Welcome to the Password Generator")

    
    try:
        length = int(input("Enter desired password length: "))
        if length <= 0:
            print(" Password length must be greater than 0.")
            return
    except ValueError:
        print(" Please enter a valid number.")
        return

   
    characters = string.ascii_letters + string.digits + string.punctuation

   
    password = ''.join(random.choice(characters) for _ in range(length))

    
    print(f"\n Generated Password: {password}")


generate_password()
