import re

text = """
Yugesh A
yugesh@gmail.com
9876543210
242237
2024-2027
"""

# 1. Name
name = re.findall(r'[A-Za-z ]+', text)

# 2. Email
email = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text)

# 3. Phone Number
phone = re.findall(r'\b\d{10}\b', text)

# 4. Roll Number (6 digits)
roll = re.findall(r'\b\d{6}\b', text)

# 5. Batch
batch = re.findall(r'\b\d{4}-\d{4}\b', text)

print("Name:", name)
print("Email:", email)
print("Phone:", phone)
print("Roll Number:", roll)
print("Batch:", batch)