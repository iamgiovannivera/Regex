# 1. Python Regular Expressions Mastery



# import re

# text = "Contact emails are: john.doe@example.com and jane.doe@example.com."
# emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", text, re.IGNORECASE)
# print(emails)
# This code uses re.IGNORECASE to handle different cases in email addresses.




# 2. Python Regular Expressions Deep Dive



# import re

# text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com"
# emails = re.findall(r"\b[A-Za-z0-9._%+-]+@(?!exclude\.com)[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", text)
# print(emails)
# This regex pattern r"\b[A-Za-z0-9._%+-]+@(?!exclude\.com)[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b" uses a negative lookahead (?!exclude\.com) to exclude email addresses from 'exclude.com'.




# 3. Advanced Text Processing with Python Regex




# import re

# text = "Name: John Doe; Age: 30; Occupation: Engineer; Location: New York"
# match = re.search(r"Occupation: ([^;]+)", text)
# if match:
#     occupation = match.group(1)
#     print(f"Occupation: {occupation}")
# else:
#     print("Occupation not found.")
# This code uses re.search() to find the key 'Occupation' and extract its value.




# 4. Python Regex Challenge:





# descriptions = [
#     "Smartphone with 6-inch screen and 128GB memory",
#     "Cotton t-shirt in medium size",
#     "Stainless steel kitchen knife set"
# ]

# tags = {
#     "Electronics": ["Smartphone", "screen", "memory"],
#     "Apparel": ["t-shirt", "Cotton"],
#     "Home & Kitchen": ["kitchen", "knife"]
# }

# def tag_product(description):
#     for tag, keywords in tags.items():
#         for keyword in keywords:
#             if keyword.lower() in description.lower():
#                 return tag
#     return "Other"

# for description in descriptions:
#     product_tag = tag_product(description)
#     print(f"Description: {description}")
#     print(f"Tag: {product_tag}\n")