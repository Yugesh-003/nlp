import re

# Read content from a text file
text = """
Employee Contact Information

Name: John Smith
Email: john.smith@example.com
Phone: 9876543210

Name: Alice Johnson
Email: alice_johnson@gmail.com
Phone: (123) 456-7890
"""

# Regular expression patterns
email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
phone_pattern = r'\b\d{10}\b|\(\d{3}\)\s?\d{3}-\d{4}|\d{3}[-.\s]\d{3}[-.\s]\d{4}'

# Find all matches
emails = re.findall(email_pattern, text)
phones = re.findall(phone_pattern, text)

# Print the results
print("📧 Email addresses found:")
for email in emails:
    print(email)

print("\n📞 Phone numbers found:")
for phone in phones:
    print(phone)
