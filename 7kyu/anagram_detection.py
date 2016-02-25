# http://www.codewars.com/kata/529eef7a9194e0cbc1000255/

def all_letters_contained(first_word, second_word):
    is_contained = True
    for letter in first_word:
        is_contained = is_contained and letter.lower() in second_word.lower()
    return is_contained


def is_anagram(test, original):
    return all_letters_contained(test, original) and all_letters_contained(original, test)
