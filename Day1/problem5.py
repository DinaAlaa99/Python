from os import remove


def removeVowels(string):
    vowels=['a','i','e','o','u']
    result = [letter for letter in string if letter.lower() not in vowels]
    result = ''.join(result)
    print(result)

removeVowels("Dina")