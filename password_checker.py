import re

password= input("Enter your password:")

#conditions
length_error=len(password)<8
digital_error=re.search(r"\d",password) is None
char_error=re.search(r"[A-Z]",password) is None
specialchar_error=re.search(r"[*&%$#@!~]",password) is None

#conditions checking
if not(length_error or digital_error or char_error or specialchar_error):
    print("Password is strong 💪")
else:
    print("Password is weak ⚠️")

    print("\nIssues found")
    if length_error:
        print("Password must be 8 letters long")
    if digital_error:
        print("Atleast one digit must be there")
    if char_error:
        print("Atleast one uppercase character")
    if specialchar_error:
        print("Atleast one special character")


    