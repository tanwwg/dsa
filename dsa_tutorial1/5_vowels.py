def is_vowel(x): return x == "a" or x == "e" or x == "i" or x == "o" or x == "u"
def count_vowels(text): return sum([is_vowel(x) for x in list(text)])

print(count_vowels("Hello"))

