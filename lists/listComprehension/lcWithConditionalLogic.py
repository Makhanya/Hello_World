numbers = [1, 2, 3, 4, 5, 6]

evens = [num for num in numbers if num % 2 == 0]

odds = [num for num in numbers if num % 2 != 0]

print(f"Even numbers: {evens}")

print(f"Odd numbers: {odds}")

print([num*2 if num % 2 == 0 else num/2 for num in numbers])

with_vowels = "This is so much fun!"
print(''.join(char for char in with_vowels if char not in "aeiou"))

print(' '.join(["cool", "dude"]))
