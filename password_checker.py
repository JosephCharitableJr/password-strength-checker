import re

print("=== Password Strength Checker ===")

password = input("Enter a password: ")

strength = 0

# Length check
if len(password) >= 8:
    strength += 1
else:
    print("❌ Password should be at least 8 characters long.")

# Uppercase check
if re.search(r"[A-Z]", password):
    strength += 1
else:
    print("❌ Add at least one uppercase letter.")

# Lowercase check
if re.search(r"[a-z]", password):
    strength += 1
else:
    print("❌ Add at least one lowercase letter.")

# Number check
if re.search(r"[0-9]", password):
    strength += 1
else:
    print("❌ Add at least one number.")

# Special character check
if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
    strength += 1
else:
    print("❌ Add at least one special character.")

# Final strength rating
print("\nPassword Strength Result:")

if strength == 5:
    print("✅ Strong Password")
elif strength >= 3:
    print("⚠️ Medium Password")
else:
    print("❌ Weak Password")
