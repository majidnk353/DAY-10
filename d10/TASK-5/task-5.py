#string methods
#--------------

#1 capitalize()
#------------
Capitalizes the first letter of the string and makes the rest lowercase.
Example:


text = "hello world"
print(text.capitalize())  # Output: "Hello world"

#2 casefold()
#------------
Converts the string to lowercase for case-insensitive comparisons.
Example:

text = "HELLO WORLD"
print(text.casefold())  # Output: "hello world"

#3 center(width, fillchar)
#-------------------------
Centers the string in a field of a given width, filling extra space with a specified character.
Example:

text = "hello"
print(text.center(10, '*'))  # Output: "**hello***"

#4 encode(encoding='utf-8', errors='strict')
#---------------------------------------------
Encodes the string into bytes using the specified encoding.
Example:

text = "hello"
print(text.encode('utf-8'))  # Output: b'hello'

#5 endswith(suffix, start, end)
#---------------------------------------------
Checks if the string ends with the specified suffix.
Example:

text = "hello world"
print(text.endswith("world"))  # Output: True

#6 expandtabs(tabsize)
#---------------------------------------------
Replaces tabs with spaces up to a specified tab size.
Example:

text = "hello\tworld"
print(text.expandtabs(4))  # Output: "hello   world"

#7 find(sub, start, end)
#---------------------------------------------
Finds the first occurrence of a substring and returns its index, or -1 if not found.
Example:

text = "hello world"
print(text.find("world"))  # Output: 6

#8 format(*args, **kwargs)
#---------------------------------------------
Definition: Formats the string by inserting values into placeholders.
Example:

text = "Hello, {}!"
print(text.format("Alice"))  # Output: "Hello, Alice!"

#9 format_map(mapping)
#---------------------------------------------
Formats the string using a dictionary for substitutions.
Example:

text = "Hello, {name}!"
mapping = {'name': 'Bob'}
print(text.format_map(mapping))  # Output: "Hello, Bob!"

#10 index(sub, start, end)
#---------------------------------------------
Finds the first occurrence of a substring and returns its index; raises an error if not found.
Example:

text = "hello world"
print(text.index("world"))  # Output: 6

#11 isalnum()
#---------------------------------------------
Checks if all characters in the string are letters or digits.
Example:

text = "hello123"
print(text.isalnum())  # Output: True

#12 isalpha()
#---------------------------------------------
Checks if all characters in the string are letters.
Example:

text = "hello"
print(text.isalpha())  # Output: True

#13 isdigit()
#---------------------------------------------
Checks if all characters in the string are digits.
Example:

text = "12345"
print(text.isdigit())  # Output: True

#14 isspace()
#---------------------------------------------
Checks if all characters in the string are whitespace.
Example:

text = "   "
print(text.isspace())  # Output: True

#15 join(iterable)
#---------------------------------------------
Joins elements of an iterable into a single string, using the string as a separator.
Example:

words = ["hello", "world"]
print(" ".join(words))  # Output: "hello world"

#16 ljust(width, fillchar)
#---------------------------------------------
Left-justifies the string in a field of a given width, filling with a specified character.
Example:

text = "hello"
print(text.ljust(10, '*'))  # Output: "hello*****"

#17 lower()
#---------------------------------------------
Converts all characters in the string to lowercase.
Example:

text = "HELLO WORLD"
print(text.lower())  # Output: "hello world"

#18 lstrip(chars)
#---------------------------------------------
Removes leading characters (whitespace by default) from the string.
Example:

text = "   hello"
print(text.lstrip())  # Output: "hello"

#19 replace(old, new, count)
#---------------------------------------------
Replaces occurrences of a substring with a new substring.
Example:

text = "hello world"
print(text.replace("world", "there"))  # Output: "hello there"

#20 strip(chars)
#---------------------------------------------
Removes leading and trailing characters (whitespace by default) from the string.
Example:

text = "   hello   "
print(text.strip())  # Output: "hello"






'''
replace(old, new, count): Replaces specified substrings in the original string.
split(sep, maxsplit)    : Splits a string into a list of substrings based on a separator.
remove(value)           : Removes the first occurrence of a specified value from a list (not a string method).
join(iterable)          : Joins a list of strings into a single string, with the original string used as the separator.

'''



















