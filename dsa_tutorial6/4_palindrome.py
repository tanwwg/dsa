def isPalindrome( x ):
    if len(x) <= 1: return True
    return isPalindrome(x[1:-1]) if x[0] == x[-1] else False

print(isPalindrome("madam"))
print(isPalindrome("apple"))
