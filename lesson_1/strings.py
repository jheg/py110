"""
Strings represent a sequence of characters. A string is an ordered collection 
of characters. Strings are immutable. 
"""

greeting = "Hello, world!"
print(greeting[0])
# greeting[99] # IndexError: string index out of range
# greeting[0] = "h" # TypeError: 'str' object does not support item assignment

# strings can be reassigned
greeting = "What's up, Doc?"

