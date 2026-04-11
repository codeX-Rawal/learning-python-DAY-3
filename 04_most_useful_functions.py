# 📘 Most Used String Functions in Python

# 1. lower() → converts to lowercase
text = "HELLO"
print(text.lower())   # hello

# 2. upper() → converts to uppercase
text = "hello"
print(text.upper())   # HELLO

# 3. strip() → removes spaces
text = "  hello  "
print(text.strip())   # hello

# 4. replace() → replaces value
text = "hello world"
print(text.replace("world", "Python"))   # hello Python

# 5. split() → converts string to list
text = "a,b,c"
print(text.split(","))   # ['a', 'b', 'c']

# 6. join() → joins list into string
lst = ['a', 'b', 'c']
print(",".join(lst))   # a,b,c

# 7. find() → finds position
text = "hello"
print(text.find("e"))   # 1

# 8. count() → counts occurrences
text = "hello"
print(text.count("l"))   # 2

# 9. startswith() → checks start
text = "hello"
print(text.startswith("he"))   # True

# 10. endswith() → checks end
text = "hello"
print(text.endswith("lo"))   # True

# 11. isalpha() → only letters
text = "hello"
print(text.isalpha())   # True

# 12. isdigit() → only numbers
text = "123"
print(text.isdigit())   # True

# 13. title() → capitalize words
text = "hello world"
print(text.title())   # Hello World

# 14. capitalize() → first letter capital
text = "hello"
print(text.capitalize())   # Hello