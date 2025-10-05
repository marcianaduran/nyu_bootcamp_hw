# 1. Write a program that takes a word as an input and print the number of vowels in the word.

word = input('Please enter a word: ')
vowels = 'aeiouAEIOU'
vowel_count = 0
for letter in word:
    if letter in vowels:
        vowel_count += 1
print('The number of vowels in the word are', vowel_count)

# 2. Iterate through the following list of animals and print each one in all caps.

animals=['tiger', 'elephant', 'monkey', 'zebra', 'panther']
for animal in animals:
    print(animal.upper())

# 3. Write a program that iterates from 1 to 20, printing each number and whether it's odd or even.

for i in range(1, 21):
    if i % 2 == 0:
        print(i, 'is even')
    else:
        print(i, 'is odd')

# 4. Write a program to check if a string is a palindrome or not.

def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

is_string = input('Please enter a string: ')

print(is_string)
if is_palindrome(is_string):
    print(f'"{is_string}" is a palindrome.')
else:
    print(f'"{is_string}" is not a palindrome.')

# 5. Write a function sum_of_integers(a, b) that takes two integers as input from the user and returns their sum. (optional)

def sum_of_integers(a, b):
    return a + b

a = int(input('Enter the first integer: '))
b = int(input('Enter the second integer: '))

print('The sum of the two integers is:', sum_of_integers(a, b))