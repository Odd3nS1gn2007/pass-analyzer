from getpass import getpass

from analyzer import (
    calculate_length_score,
    calculate_character_score,
    calculate_final_score,
    classify_strength
)

from patterns import detect_patterns

from suggestions import generate_suggestions

from storage import (
    is_common_password,
    is_reused_password,
    store_password
)


def main():
    print("===== PASSWORD STRENGTH ANALYZER =====\n")

    password = getpass("Enter Password: ")

    # Common password check
    if is_common_password(password):
        print("\nStatus      : REJECTED")
        print("Reason      : Common password detected")
        print("Final Score : 0/50")
        return

    # Reused password check
    if is_reused_password(password):
        print("\nStatus      : REJECTED")
        print("Reason      : Password reuse detected")
        print("Final Score : 0/50")
        return

    # Length score
    length_score = calculate_length_score(password)

    # Character diversity score
    character_score = calculate_character_score(password)

    # Pattern detection
    penalties, detected_patterns = detect_patterns(password)

    # Final score
    final_score = calculate_final_score(
        length_score,
        character_score,
        penalties
    )

    # Strength classification
    strength = classify_strength(final_score)

    # Suggestions
    suggestions = generate_suggestions(
        password,
        detected_patterns
    )

    # Display report
    print("\n===== PASSWORD ANALYSIS =====\n")

    print(f"Length Score        : {length_score}/25")
    print(f"Character Score     : {character_score}/25")
    print(f"Pattern Penalty     : -{penalties}")

    print(f"\nFinal Score         : {final_score}/50")
    print(f"Strength            : {strength}")

    print("\nSuggestions:")

    if suggestions:
        for suggestion in suggestions:
            print(f"- {suggestion}")
    else:
        print("- No suggestions needed")

    # Store password hash
    store_password(password)


if __name__ == "__main__":
    main()