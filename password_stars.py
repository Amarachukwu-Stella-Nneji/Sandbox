MINIMUM_LENGTH = 5
password = input("Enter a password: ")
while len(password) < MINIMUM_LENGTH:
    password = input("Enter a password: ")
asterisks = '*' * len(password)
print(f"Password: {asterisks}.")
