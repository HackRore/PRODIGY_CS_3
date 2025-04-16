# Password Complexity Checker

A Python-based tool that evaluates the strength of passwords based on multiple criteria to help users create secure passwords.

## Features

- Evaluates password strength based on:
  - Length (minimum 8 characters, recommended 12+)
  - Presence of uppercase letters (A-Z)
  - Presence of lowercase letters (a-z)
  - Presence of numbers (0-9)
  - Presence of special characters (!@#$%^&*(),.?":{}|<>)
- Provides detailed feedback for each criterion
- Calculates an overall strength score (0-7)
- Classifies passwords as Strong, Medium, or Weak

## Requirements

- Python 3.x
- No external dependencies required

## Usage

1. Run the script:
   ```bash
   python password_checker.py
   ```

2. Enter a password when prompted
3. The program will analyze the password and provide:
   - Overall strength rating
   - Score out of 7
   - Detailed feedback for each criterion

4. To exit the program, type 'quit' when prompted for a password

## Scoring System

The password is evaluated on a scale of 0-7 points:

- Length:
  - 3 points for 12+ characters
  - 2 points for 8+ characters
- 1 point each for:
  - Uppercase letters
  - Lowercase letters
  - Numbers
  - Special characters

## Strength Classification

- Strong: 6-7 points
- Medium: 4-5 points
- Weak: 0-3 points

## Example Output

```
Password Complexity Checker
---------------------------

Enter a password to check (or 'quit' to exit): MyP@ssw0rd123

Password Analysis:
Strength: Strong (6/7)

Details:
  ✓ Password length is good (12+ characters)
  ✓ Contains uppercase letters
  ✓ Contains lowercase letters
  ✓ Contains numbers
  ✓ Contains special characters
```

## Security Note

This tool is designed to help users create stronger passwords. It does not store or transmit any passwords entered during the checking process.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       