#Operators in Python >>>

x = 50
y = 25

print(f"Addition Operator = {x+y}")
print(f"Subtraction Operator = {x-y}")
print(f"Multiplication Operator= {x*y}")
print(f"Division Operator = {x/y}")
print(f"Floor Division Operator = {x//y}")
print(f"Exponential Operator  = {x**y}")

print(f"is X equal to Y {x==y}")
print(f"is X not equal to Y {x!=y}")

first_name = "najmus"
last_name = "Saquib"
full_name = first_name + last_name

print(f"full_name = {full_name}")
print(f"Length of the String full_name {len(full_name)}")
print(f"indexing of string [3] {full_name[3]}")
print(f"indexing of string [-2] {full_name[-2]}")
print(f"indexing of string [0:3] {full_name[0:3]}")

print(full_name.capitalize())
print(full_name.upper())
print(full_name.lower())
print(full_name.find("s"))
print(full_name.find("s", 0, 6))
print(full_name.isalnum())

ascii = "$"
print(ascii.isascii())

replace = "Names"
print(replace.replace("s", ""))

print(full_name.swapcase())
