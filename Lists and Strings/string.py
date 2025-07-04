"""string = "Hello World!"

# 1. split operation
spl = string.split()
print(spl)

# 2. joining operation
joining = "".join(string)
print(joining)
joining = "-".join(string)
print(joining)

# 3. replacing operation
rep = string.replace("Hello", "Bye")
print(rep)

# 4. lower case
low = string.lower()
print (low)

# 5. upper case
up = string.upper()
print(up)"""

# reversing a string
text = "hellow world!!"

rev = text[::-1]
print( rev)

# Ques - Remove duplicates from a string

dup = [1, 2, 2, 3, 4, 4, 5]

unique = list(set(dup))
# print(dup)
# print(unique)

# ques - counting vowels
text = "Data science is an interdisciplinary academic field that uses statistics, scientific computing, scientific methods, processing, scientific visualization, algorithms and systems to extract or extrapolate knowledge from potentially noisy, structured, or unstructured data."

vowels = "aeiouAEIOU"
count = sum(1 for char in text if char in vowels)
print("Number of vowels:", count)
