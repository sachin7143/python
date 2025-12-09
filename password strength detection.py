password = input("Enter password: ")

length = len(password)
has_digit = any(ch.isdigit() for ch in password)
has_upper = any(ch.isupper() for ch in password)
has_lower = any(ch.islower() for ch in password)
has_symbol = any(not ch.isalnum() for ch in password)

score = 0
if length >= 8: score += 1
if has_digit: score += 1
if has_upper: score += 1
if has_lower: score += 1
if has_symbol: score += 1

print("Strength Score:", score, "/ 5")

if score <= 2:
    print("Weak password")
elif score == 3:
    print("Medium strength")
else:
    print("Strong password!")
