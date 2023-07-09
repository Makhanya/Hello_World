# Titleize
# Write a function called titleize which accepts a string of words
# and returns a new string with the first letter of every word in
# the string capitalized.

def titleize(string):
    return ' '.join(s[0].upper() + s[1:] for s in string.split(' '))


titleize('this is awesome')  # "This Is Awesome"
titleize('oNLy cAPITALIZe fIRSt')  # "ONLy CAPITALIZe FIRSt"
