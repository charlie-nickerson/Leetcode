# Leetcode

# Things To Note in Python:
- Dictionaires cannot be used as keys because they are mutable. Instead convert them into tuples
- Make sure to always use () at the end of methods or else you will get object is not iterable errors
- Prefix and postfix methods can be useful when you have to do an operation for each element using the rest of the elements in an array
- Counter and defaultdict are super valuable in array and hashing questions. Use the collections library
- When using print statements dont forget to use .format() at the end of the string if you want to use variables in the string e.g. "{n} is a number".format(number=0) prints "0 is a number"
- The .isalnum method can be attached to end of a character to check if its an alphanumeric character (a-z, 0-9, or A-Z)
- The reversed() function returns an object not a string. If you want to get the string value just use "".join on the reversed function
- In list comprehension you can use for loops and if statements to filter out elements of an array or string e.g. [ch for ch in s.lower() if ch.isalnum()] | Refer to leetcode125.py


