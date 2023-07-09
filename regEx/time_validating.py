"""
Time Validating
Write a function called is_valid_time  that accepts a single string argument.
It should return True  if the string is formatted correctly as a time, like 3:15 or 12:48 and return False otherwise.
 Note that times can start with a single number (2:30) or two (11:18).

is_valid_time("10:45")       #True
is_valid_time("1:23")        #True
is_valid_time("10.45")       #False
is_valid_time("1999")        #False
is_valid_time("145:23")      #False
In order to return True, the string should ONLY contain the time, and no other characters

is_valid_time("it is 12:15") #False
is_valid_time("12:15")       #True
Don't worry about impossible times like 88:76, just focus on the formatting!

is_valid_time("34:55") #True

"""

import re


def is_valid_time(input):
    pattern = re.compile(r'^\d\d?:\d\d$')
    match = pattern.search(input)
    if match:
        return True
    return False


print(is_valid_time("10:45"))
print(is_valid_time("1:23"))
print(is_valid_time("10.45"))
print(is_valid_time("1999"))
print(is_valid_time("145:23"))
print(is_valid_time("its is 12:14"))
print(is_valid_time("13:15"))
print(is_valid_time("34:55"))
