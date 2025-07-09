#******************************************
# 02. Password Strength Checker          #
# Concepts: Strings, Booleans, If/Else   #
# Variables, Operators, Functions        #
#******************************************

def check_password_strength(password):
    """Check how strong a password is"""
    length = len(password)
    has_numbers = any(char.isdigit() for char in password)
    has_uppercase = any(char.isupper() for char in password)
    has_lowercase = any(char.islower() for char in password)
    
    strength_score = 0
    
    if length >= 8:
        strength_score += 1
    if has_numbers:
        strength_score += 1
    if has_uppercase:
        strength_score += 1
    if has_lowercase:
        strength_score += 1
    
    return strength_score

# Test your password
user_password = input("Enter a password to test: ")
score = check_password_strength(user_password)

print(f"Password: {'*' * len(user_password)}")  # Hide password
print(f"Length: {len(user_password)} characters")

if score >= 4:
    print("🔒 Strong password! Great job!")
elif score >= 2:
    print("🔐 Medium strength - could be better")
else:
    print("🔓 Weak password - very risky!")

print(f"Strength score: {score}/4")