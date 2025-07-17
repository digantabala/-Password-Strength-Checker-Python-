import re

def assess_password_strength(password):
    # Initialize feedback list and strength categories
    feedback = []
    strength_levels = {
        0: "Very Weak", 1: "Weak", 2: "Moderate", 
        3: "Strong", 4: "Very Strong"
    }
    
    # Criteria checks
    length = len(password)
    has_upper = bool(re.search(r'[A-Z]', password))
    has_lower = bool(re.search(r'[a-z]', password))
    has_digit = bool(re.search(r'[0-9]', password))
    has_special = bool(re.search(r'[^A-Za-z0-9]', password))
    
    # Length assessment
    if length < 8:
        feedback.append("Password is too short (min 8 characters)")
    elif length < 12:
        feedback.append("Consider increasing length to 12+ characters")
    
    # Character diversity feedback
    if not has_upper:
        feedback.append("Add uppercase letters (A-Z)")
    if not has_lower:
        feedback.append("Add lowercase letters (a-z)")
    if not has_digit:
        feedback.append("Include numbers (0-9)")
    if not has_special:
        feedback.append("Use special characters (e.g. !@#$%)")
    
    # Calculate strength score (max 4 points)
    score = 0
    if length >= 8: score += 1
    if length >= 12: score += 1
    if has_upper and has_lower: score += 1
    if has_digit and has_special: score += 1
    
    # Final strength rating
    strength = strength_levels.get(score, "Very Weak")
    
    return {
        "strength": strength,
        "score": f"{score}/4",
        "feedback": feedback,
        "length": length,
        "has_upper": has_upper,
        "has_lower": has_lower,
        "has_digit": has_digit,
        "has_special": has_special
    }

# Example usage:
if __name__ == "__main__":
    while True:
        pwd = input("\nEnter password to assess (or 'q' to quit): ")
        if pwd.lower() == 'q':
            break
            
        result = assess_password_strength(pwd)
        print(f"\nPassword Strength: {result['strength']} ({result['score']})")
        print(f"Length: {result['length']} characters")
        
        if result['feedback']:
            print("\nRecommendations:")
            for item in result['feedback']:
                print(f"- {item}")
        else:
            print("\nNo improvements needed! Excellent password.")