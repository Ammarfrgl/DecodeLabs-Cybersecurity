leaked_passwords = ["password123", "123456789", "qwerty123", "admin123", "iloveyou"]

password = input("Enter a password to check: ")

if len(password) < 8:
    print("Weak password - too short!")
else:
    if password in leaked_passwords:
        print("Weak password - this password is commonly known by hackers!")
    else:
        has_upper = any(char.isupper() for char in password)
        has_digit = any(char.isdigit() for char in password)
        has_symbol = any(char in "!@#$%^&*" for char in password)
        score = sum([has_upper, has_digit, has_symbol])
        if score == 3:
            print("Strong password! 💪")
        elif score == 2:
            print("Medium password - could be stronger!")
        else:
            print("Weak password - add uppercase, numbers and symbols!")