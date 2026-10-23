# Password Security Audit Tool

Python-based password security auditing tool for analyzing password strength and detecting common weak passwords using local test data.
## Features

- Password length analysis
- Uppercase, lowercase, digit, and special-character checks
- Security score calculation
- Strong / Moderate / Weak rating
- Common-password detection using a local test list
- Security audit report generation
- Password input is hidden using Python `getpass`

## Technologies

- Python 3
- Kali Linux
- Bash / Linux Terminal

## Testing

The tool was tested using dummy passwords only.

### Strong Password Test

Example:

`TestPassword123!`

Result:

- Score: 100/100
- Rating: STRONG
- Common-password check: PASS

### Weak Password Test

Example:

`password123`

Result:

- Score: 45/100
- Rating: WEAK
- Common-password check: WARNING

## Output

The tool generates:

`security_report.txt`

The report contains password length, character diversity, security score, rating, and common-password check results.

## Security Note

This project is intended for defensive security education and local testing only.

Never enter real passwords into development or testing tools.

## Author

Hannacybersec
