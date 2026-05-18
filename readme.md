The Password Strength Analyzer is a Python-based cybersecurity mini project developed to evaluate the strength and security of user passwords. The tool analyzes passwords based on multiple security parameters such as length, character diversity, predictability, and password reuse.

The project aims to promote secure password creation practices and demonstrate fundamental cybersecurity concepts including password security, hashing, brute-force resistance, dictionary attack prevention, and secure credential handling.

---

## Features

- Password length analysis
- Character diversity checking
- Common password detection
- Password reuse prevention
- Sequential pattern detection
- Repeated character detection
- Strength scoring system
- Dynamic password improvement suggestions
- Secure password hashing
- Binary file storage for password history

---
## Modules Description

main.py

Controls the overall execution flow of the project and handles user interaction.

analyzer.py

Performs password scoring, length analysis, character diversity analysis, and strength classification.

patterns.py

Detects predictable patterns such as sequential numbers, sequential alphabets, and repeated characters.

suggestions.py

Generates password improvement suggestions based on detected weaknesses.

storage.py

Handles password hashing, binary file storage, and password reuse detection.

common_passwords.txt

Stores a list of commonly used weak passwords used for blacklist checking.

password_history.bin

Stores hashed passwords securely in binary format for reuse prevention.

---
## Scoring System

The password strength score is calculated out of 50 points.

## Length Score (25 Points)

| Password Length | Score |
|-----------------|-------|
| < 6             | 0     |
| 6 – 7           | 5     |
| 8 – 9           | 10    |
| 10 – 11         | 15    |
| 12 – 14         | 20    |
| 15 or more      | 25    |

---

## Character Diversity Score (25 Points)

| Character Type | Points |
|----------------|--------|
| Lowercase      | 5      |
| Uppercase      | 5      |
| Numbers        | 5      |
| Special Symbols| 5      |
| All Combined   | 5      |

---

## Pattern Penalties

| Weak Pattern | Penalty |
|--------------|---------|
| Sequential Numbers | -5 |
| Sequential Alphabets | -5 |
| Repeated Characters | -5 |

**Instant Rejection Conditions**
Common password detected
Password reuse detected

---
## Future Enhancements
- Graphical User Interface (GUI)
- Database integration
- Multi-user authentication system
- Password generation system
- Exportable report

---