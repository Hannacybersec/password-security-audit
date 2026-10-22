#!/usr/bin/env python3

import getpass
import string

print("====================================")
print("      Password Security Audit")
print("====================================")

print("[+] Password Security Audit Tool")
print("[+] Local defensive security testing")
print()

password = getpass.getpass("Enter a dummy/test password: ")

print()
print("[+] Password received.")
print(f"[+] Password length: {len(password)}")

if len(password) >= 12:
    print("[PASS] Password length is strong.")
elif len(password) >= 8:
    print("[WARN] Password length is acceptable but could be stronger.")
else:
    print("[FAIL] Password is too short.")

has_upper = any(c.isupper() for c in password)
has_lower = any(c.islower() for c in password)
has_digit = any(c.isdigit() for c in password)
has_special = any(c in string.punctuation for c in password)

print()
print("Character Diversity:")
print(f"  Uppercase: {'YES' if has_upper else 'NO'}")
print(f"  Lowercase: {'YES' if has_lower else 'NO'}")
print(f"  Digits: {'YES' if has_digit else 'NO'}")
print(f"  Special characters: {'YES' if has_special else 'NO'}")

score = 0

if len(password) >= 12:
    score += 25
elif len(password) >= 8:
    score += 15

if has_upper:
    score += 15

if has_lower:
    score += 15

if has_digit:
    score += 15

if has_special:
    score += 15

if len(password) >= 16:
    score += 15

print()
print("Security Score:")
print(f"  Score: {score}/100")

if score >= 80:
    rating = "STRONG"
elif score >= 60:
    rating = "MODERATE"
else:
    rating = "WEAK"

print(f"  Rating: {rating}")

try:
    with open("common_passwords.txt", "r") as file:
        common_passwords = {
            line.strip().lower()
            for line in file
            if line.strip()
        }

    if password.lower() in common_passwords:
        common_warning = "WARNING: Password appears in the common-password list."
        print()
        print("[WARNING] Password appears in the common-password list.")
        print("[WARNING] Choose a less predictable password.")
    else:
        common_warning = "PASS: Password was not found in the common-password list."
        print()
        print("[PASS] Password was not found in the common-password list.")

except FileNotFoundError:
    common_warning = "ERROR: common_passwords.txt not found."
    print()
    print("[ERROR] common_passwords.txt not found.")

report = f"""
Password Security Audit Report
================================

Password Length: {len(password)}

Character Diversity:
  Uppercase: {'YES' if has_upper else 'NO'}
  Lowercase: {'YES' if has_lower else 'NO'}
  Digits: {'YES' if has_digit else 'NO'}
  Special Characters: {'YES' if has_special else 'NO'}

Security Score: {score}/100
Security Rating: {rating}

Common Password Check:
  {common_warning}
"""

with open("security_report.txt", "w") as file:
    file.write(report)

print()
print("[+] Audit report saved as: security_report.txt")
