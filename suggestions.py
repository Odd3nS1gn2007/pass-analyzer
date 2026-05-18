import re


def generate_suggestions(password, detected_patterns):
    suggestions = []

    # Length suggestions
    if len(password) < 8:
        suggestions.append("Increase password length")

    elif len(password) < 12:
        suggestions.append("Consider using 12 or more characters")

    # Character diversity suggestions
    if not re.search(r"[a-z]", password):
        suggestions.append("Add lowercase letters")

    if not re.search(r"[A-Z]", password):
        suggestions.append("Add uppercase letters")

    if not re.search(r"[0-9]", password):
        suggestions.append("Include numeric digits")

    if not re.search(r"[^A-Za-z0-9]", password):
        suggestions.append("Add special characters")

    # Pattern suggestions
    if "Sequential Numbers" in detected_patterns:
        suggestions.append("Avoid sequential number patterns")

    if "Sequential Alphabets" in detected_patterns:
        suggestions.append("Avoid alphabetical sequences")

    if "Repeated Characters" in detected_patterns:
        suggestions.append("Avoid repeated characters")

    return suggestions