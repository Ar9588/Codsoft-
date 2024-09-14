#Task 2 Password generator
import random
import string

# Function to generate password
def generate_password(length):
    # Characters to choose from: uppercase, lowercase, digits, and punctuation
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Ensuring at least one character from each category
    password = [
        random.choice(string.ascii_uppercase),   # at least one uppercase letter
        random.choice(string.ascii_lowercase),   # at least one lowercase letter
        random.choice(string.digits),            # at least one digit
        random.choice(string.punctuation)        # at least one special character
    ]

    # Adding random characters to meet the desired length
    password += random.choices(characters, k=length - 4)

    # Shuffle the password list to avoid predictable patterns
    random.shuffle(password)

    # Convert list to string
    return ''.join(password)

# Main program
if __name__ == "__main__":
    try:
        length = int(input("Enter the length of the password (minimum 4 characters): "))
        if length < 4:
            print("Password length should be at least 4.")
        else:
            password = generate_password(length)
            print(f"Generated Password: {password}")
    except ValueError:
        print("Please enter a valid number for password length.")
