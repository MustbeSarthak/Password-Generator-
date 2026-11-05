"""
Password Generator
Auspify Technologies - Python Developer Internship
"""
import secrets
import string

# Character sets
LOWERCASE = string.ascii_lowercase
UPPERCASE = string.ascii_uppercase
DIGITS = string.digits
SYMBOLS = string.punctuation

def generate_password(length):
    """Generate a secure random password."""

    # Ensure at least one character from each category
    password = [secrets.choice(LOWERCASE),secrets.choice(UPPERCASE),secrets.choice(DIGITS),secrets.choice(SYMBOLS)]

    # Combine all character categories
    all_characters = LOWERCASE + UPPERCASE + DIGITS + SYMBOLS

    # Fill remaining positions because the 4 characters are already there
    for _ in range(length - 4):
        password.append(secrets.choice(all_characters))

    # Shuffle characters to avoid predictable positions
    secrets.SystemRandom().shuffle(password)
    return ''.join(password)


def save_password(password):
    """Save generated password to a text file."""
    with open("passwords.txt", "a") as file:
        file.write(password + "\n")


def main():
    print("=" * 40)
    print("       PASSWORD GENERATOR")
    print("=" * 40)

    # Get password length
    while True:
        try:
            length = int(input("\nEnter password length (minimum 4): "))
            if length < 4:
                print("Password length must be at least 4.")
            else:
                break
        except ValueError:
            print("Please enter a valid number.")

    # Get number of passwords
    while True:
        try:
            num_passwords = int(input("How many passwords do you want? "))
            if num_passwords <= 0:
                print("Enter a number greater than zero.")
            else:
                break
        except ValueError:
            print("Please enter a valid number.")

    print("\nGenerating passwords...\n")

    # Generate passwords
    for i in range(num_passwords):
        password = generate_password(length)
        print(f"Password {i + 1}: {password}")

    # Ask whether to save the password
    while True:
        choice = input("Do you want to save this password? (Y/N): ").strip().lower()
        if choice in ("y", "yes"):
            save_password(password)
            print("Password saved successfully!\n")
            break
        elif choice in ("n", "no"):
            print("Password not saved.\n")
            break
        else:
            print("Please enter Y or N.")

    print("=" * 40)
    print("Password generation completed!")
    print("=" * 40)


if __name__ == "__main__":
    main()