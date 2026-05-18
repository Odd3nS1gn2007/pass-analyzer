def has_sequential_numbers(password):
    sequences = [
    "012", "123", "234", "345",
    "456", "567", "678", "789",

    "0123", "1234", "2345", "3456",
    "4567", "5678", "6789"
]

    for sequence in sequences:
        if sequence in password:
            return True

    return False


def has_sequential_alphabets(password):
    password = password.lower()

    sequences = [
    "abc", "bcd", "cde", "def",
    "efg", "fgh", "ghi", "hij",
    "ijk", "jkl", "klm", "lmn",
    "mno", "nop", "opq", "pqr",
    "qrs", "rst", "stu", "tuv",
    "uvw", "vwx", "wxy", "xyz",

    "abcd", "bcde", "cdef", "defg",
    "efgh", "fghi", "ghij", "hijk",
    "ijkl", "jklm", "klmn", "lmno",
    "mnop", "nopq", "opqr", "pqrs",
    "qrst", "rstu", "stuv", "tuvw",
    "uvwx", "vwxy", "wxyz"
]

    for sequence in sequences:
        if sequence in password:
            return True

    return False


def has_repeated_characters(password):
    for character in password:
        if character * 4 in password:
            return True

    return False


def detect_patterns(password):
    penalties = 0
    detected_patterns = []

    if has_sequential_numbers(password):
        penalties += 5
        detected_patterns.append("Sequential Numbers")

    if has_sequential_alphabets(password):
        penalties += 5
        detected_patterns.append("Sequential Alphabets")

    if has_repeated_characters(password):
        penalties += 5
        detected_patterns.append("Repeated Characters")

    return penalties, detected_patterns