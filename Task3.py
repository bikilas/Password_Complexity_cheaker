import re
#we us re  => regulara expresion(regex)
def check_password_complexity(password):
    """
    This function checks the complexity of the password based on:
    - Minimum length of 8 characters.
    - At least one uppercase letter.
    - At least one lowercase letter.
    - At least one digit.
    - At least one special character.
    """
    strength = 0
    feedback = []

    # Check password length
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")

    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.")

    # Check for digits
    if re.search(r'[0-9]', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one digit.")

    # Check for special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one special character.")
    
    # Feedback and Strength Level
    if strength == 5:
        return "Strong Password", feedback
    elif 3 <= strength < 5:
        return "Moderate Password", feedback
    else:
        return "Weak Password", feedback

def main():
    """
    Main function to prompt the user for a password and check its complexity.
    Loops until a strong password is entered.
    """
    while True:
        user_password = input("Please enter your password: ")
        strength, advice = check_password_complexity(user_password)
        print(f"Password Strength: {strength}")
        
        if strength == "Strong Password":
            print("Your password meets all the requirements.")
            break  # Exit the loop if the password is strong
        
        if advice:
            print("Suggestions to improve your password:")
            for item in advice:
                print(f"- {item}")
        print("\nTry again.\n")  # Prompt to try again

# Run the main function
if __name__ == "__main__":
    main()
