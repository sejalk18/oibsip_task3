import random
import string

def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    """
    Function to generate a random password based on user-defined criteria.
    :param length: Length of the password (int)
    :param use_letters: Whether to include letters in the password (bool)
    :param use_numbers: Whether to include numbers in the password (bool)
    :param use_symbols: Whether to include symbols in the password (bool)
    :return: Generated password (string)
    """
    characters = ""
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        print("Error: Please select at least one character type.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    length = int(input("Enter the length of the password: "))
    use_letters = input("Include letters? (yes/no): ").lower() == "yes"
    use_numbers = input("Include numbers? (yes/no): ").lower() == "yes"
    use_symbols = input("Include symbols? (yes/no): ").lower() == "yes"

    password = generate_password(length, use_letters, use_numbers, use_symbols)
    if password:
        print("Your generated password is:", password)

if __name__ == "__main__":
    main()
