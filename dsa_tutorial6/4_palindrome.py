def isPalindrome( x ):
    if len(x) <= 1: return True
    if x[0] == x[-1]:
        return isPalindrome(x[1:-1])
    else:
        return False

print(isPalindrome("madam"))
print(isPalindrome("apple"))
