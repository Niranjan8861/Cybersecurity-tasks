def checkstrength(password):
    length = len(password)
    has_lowercase = any(c.islower() for c in password)
    has_uppercase = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special_char = any(c in "!@#$%^&*()_+-=[]{}|;:'\",.<>?/" for c in password)  
    score = 0
    if length >= 8:
        score += 1
    if has_lowercase:
        score += 1
    if has_uppercase:
        score += 1
    if has_digit:
        score += 1
    if has_special_char:
        score += 1
        
    if score >= 4:
        return "Strong password! 👍"
    elif score >= 3:
        return "Moderate password. Consider adding more complexity."
    else:
        return "Weak password. Please improve it."

# Example usage
user_password = input("Enter your password: ")
strength_feedback = checkstrength(user_password)
print(strength_feedback)
