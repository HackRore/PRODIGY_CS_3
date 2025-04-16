import re
import sys
from getpass import getpass

def check_password_strength(password):
    # Input validation
    if not isinstance(password, str):
        raise TypeError("Password must be a string")
    
    if not password:
        raise ValueError("Password cannot be empty")
    
    # Initialize strength score and feedback
    score = 0
    feedback = []
    warnings = []
    
    # Check length
    if len(password) >= 12:
        score += 3
        feedback.append("✓ Password length is good (12+ characters)")
    elif len(password) >= 8:
        score += 2
        feedback.append("✓ Password length is acceptable (8+ characters)")
    else:
        feedback.append("✗ Password is too short (minimum 8 characters)")
    
    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        score += 1
        feedback.append("✓ Contains uppercase letters")
    else:
        feedback.append("✗ Missing uppercase letters")
    
    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        score += 1
        feedback.append("✓ Contains lowercase letters")
    else:
        feedback.append("✗ Missing lowercase letters")
    
    # Check for numbers
    if re.search(r'[0-9]', password):
        score += 1
        feedback.append("✓ Contains numbers")
    else:
        feedback.append("✗ Missing numbers")
    
    # Check for special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
        feedback.append("✓ Contains special characters")
    else:
        feedback.append("✗ Missing special characters")
    
    # Additional security checks
    if re.search(r'(.)\1{2,}', password):
        warnings.append("⚠ Warning: Password contains repeated characters")
    
    if re.search(r'[a-z]{3,}|[A-Z]{3,}|[0-9]{3,}', password):
        warnings.append("⚠ Warning: Password contains consecutive characters of the same type")
    
    if len(password) > 50:
        warnings.append("⚠ Warning: Password is unusually long")
    
    # Check for common patterns
    common_patterns = [
        r'^[a-z]+$',  # All lowercase
        r'^[A-Z]+$',  # All uppercase
        r'^[0-9]+$',  # All numbers
        r'^[!@#$%^&*(),.?":{}|<>]+$'  # All special characters
    ]
    
    for pattern in common_patterns:
        if re.match(pattern, password):
            warnings.append("⚠ Warning: Password uses only one type of character")
            break
    
    # Determine strength level
    if score >= 6:
        strength = "Strong"
    elif score >= 4:
        strength = "Medium"
    else:
        strength = "Weak"
    
    return {
        "score": score,
        "strength": strength,
        "feedback": feedback,
        "warnings": warnings
    }

def main():
    print("Password Complexity Checker")
    print("---------------------------")
    print("Note: For security, your password will not be displayed as you type.")
    print("Type 'quit' to exit the program.\n")
    
    while True:
        try:
            # Use getpass for secure password input
            password = getpass("Enter a password to check: ")
            
            if password.lower() == 'quit':
                print("\nExiting program...")
                break
            
            result = check_password_strength(password)
            
            print("\nPassword Analysis:")
            print(f"Strength: {result['strength']} ({result['score']}/7)")
            print("\nDetails:")
            for item in result['feedback']:
                print(f"  {item}")
            
            if result['warnings']:
                print("\nWarnings:")
                for warning in result['warnings']:
                    print(f"  {warning}")
            
            print("\n" + "="*50)
            
        except KeyboardInterrupt:
            print("\n\nProgram interrupted by user. Exiting...")
            sys.exit(0)
        except Exception as e:
            print(f"\nError: {str(e)}")
            print("Please try again.\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nProgram interrupted by user. Exiting...")
        sys.exit(0) 