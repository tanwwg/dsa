text = "abcdeeiou"

list(text)

def is_vowel(x): return x == "a" or x == "e" or x == "i" or x == "o" or x == "u"
def map_vowel(data): return [is_vowel(x) for x in data]

map_vowel(list(text))
