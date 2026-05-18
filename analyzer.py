import re


def calculate_length_score(password):
    length = len(password)

    if length < 6:
        return 0

    elif length <= 7:
        return 5

    elif length <= 9:
        return 10

    elif length <= 11:
        return 15

    elif length <= 14:
        return 20

    else:
        return 25


def calculate_character_score(password):
    score = 0

    has_lowercase = re.search(r"[a-z]", password)
    has_uppercase = re.search(r"[A-Z]", password)
    has_number = re.search(r"[0-9]", password)
    has_special = re.search(r"[^A-Za-z0-9]", password)

    if has_lowercase:
        score += 5

    if has_uppercase:
        score += 5

    if has_number:
        score += 5

    if has_special:
        score += 5

    if (
        has_lowercase and
        has_uppercase and
        has_number and
        has_special
    ):
        score += 5

    return score


def calculate_final_score(length_score, character_score, penalties):
    final_score = length_score + character_score - penalties

    if final_score < 0:
        final_score = 0

    if final_score > 50:
        final_score = 50

    return final_score


def classify_strength(score):
    if score == 0:
        return "REJECTED"

    elif score <= 15:
        return "WEAK"

    elif score <= 30:
        return "MODERATE"

    elif score <= 40:
        return "STRONG"

    else:
        return "VERY STRONG"