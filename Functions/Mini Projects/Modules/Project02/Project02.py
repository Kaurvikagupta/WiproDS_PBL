# Import the module and test the functions.

import name_module

name = input("Enter a name: ")

print(name_module.ispalindrome(name))

print("No of vowels:", name_module.count_the_vowels(name))

frequency = name_module.frequency_of_letters(name)

print("Frequency of letters:")

for letter, count in frequency.items():
    print(letter, "-", count)