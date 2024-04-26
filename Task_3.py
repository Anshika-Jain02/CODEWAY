'''
A password generator is a useful tool that generates strong and random passwords for
users. This project aims to create a password generator application using Python,
allowing users to specify the length and complexity of the password.

'''
import random
import string

def generate_password(length):
    # Define the characters to choose from for the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate the password by randomly selecting characters
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def main():
    try:
        length = int(input("Enter the desired length of the password: "))
        if length <= 0:
            print("Invalid length. Please enter a positive integer.")
            return
    except ValueError:
        print("Invalid input. Please enter a valid integer for the length.")
        return

    password = generate_password(length)
    print("Generated password:", password)

if __name__ == "__main__":
    main()
