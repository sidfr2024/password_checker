# password_checker
This Python script validates the strength of a password based on common security rules. It uses the re (regular expressions) module to check whether the password meets all required conditions. The program provides clear feedback and lists any issues found, helping users create stronger, more secure passwords.
Features

Checks if the password length is at least 8 characters

Ensures the password contains at least one digit

Requires at least one uppercase letter

Verifies that the password includes at least one special character (* & % $ # @ ! ~)

Displays a message indicating whether the password is strong

If the password is weak, it shows the exact issues so the user can improve it

How It Works

The script uses the Python re module for pattern matching:

\d is used to detect digits

[A-Z] is used to detect uppercase letters

[*&%$#@!~] is used to detect required special characters

Each rule is checked individually, and the script determines the password strength based on the results.

Code Overview
import re

password= input("Enter your password:")

#conditions
length_error=len(password)<8
digital_error=re.search(r"\d",password) is None
char_error=re.search(r"[A-Z]",password) is None
specialchar_error=re.search(r"[*&%$#@!~]",password) is None

#conditions checking
if not(length_error or digital_error or char_error or specialchar_error):
    print("Password is strong")
else:
    print("Password is weak")

    print("\nIssues found")
    if length_error:
        print("Password must be 8 letters long")
    if digital_error:
        print("At least one digit must be included")
    if char_error:
        print("At least one uppercase character is required")
    if specialchar_error:
        print("At least one special character is required")

How to Run

Install Python 3

Save the script as password_checker.py

Open a terminal or command prompt

Run the script using:

python password_checker.py


Enter a password when prompted

Review the feedback provided by the program

Learning Objectives

This project helps learners understand:

Basic input handling in Python

Using regular expressions for validation

Implementing logical conditions

Writing clear, user-friendly CLI programs
