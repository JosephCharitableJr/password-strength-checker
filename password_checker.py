import re

print("===================================")
print("      Password Strength Checker")
print("===================================")

password = input("Enter a password: ")

strength = 0

# Check password length
if len(password) >= 8:
    strength += 1
else:
    print("❌ Password should be at least 8 characters long.")

# Check for uppercase letter
if re.search(r"[A-Z]", password):
    strength += 1
else:
    print("❌ Add at least one uppercase letter.")

# Check for lowercase letter
if re.search(r"[a-z]", password):
    strength += 1
else:
    print("❌ Add at least one lowercase letter.")

# Check for number
if re.search(r"[0-9]", password):
    strength += 1
else:
    print("❌ Add at least one number.")

# Check for special character
if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
    strength += 1
else:
    print("❌ Add at least one special character.")

# Display final result
print("\n===================================")
print("      Password Strength Result")
print("===================================")

if strength == 5:
    print("✅ Strong Password")
elif strength >= 3:
    print("⚠️ Medium Password")
else:
    print("❌ Weak Password")
