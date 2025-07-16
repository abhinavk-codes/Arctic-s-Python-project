# Program: Password Strength Checker

def has_digits_and_special_chars(s):
    has_digit = False
    has_special = False

    for i in range(len(s)):
        ch = s[i]
        if ch.isdigit():
            has_digit = True
        elif not ch.isalnum():
            has_special = True
        if has_digit and has_special:
            return True
    return False

# Take input
password = input("Enter a password: ")

# Check length
if len(password) < 6:
    print("❌ Weak password! (Too short)")
elif 6 <= len(password) <= 10:
    if has_digits_and_special_chars(password):
        print("✅ Medium-Strong password! (Has digits & special chars)")
    else:
        print("⚠️ Medium password, but try adding digits & special chars!")
else:  # len(password) > 10
    if has_digits_and_special_chars(password):
        print("💪 Strong password! Good job!")
    else:
        print("⚠️ Long password, but missing digits or special chars.")

