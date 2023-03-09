def palindrome(s):
    k = ''.join(reversed(s))
    if (s == k): print("Is Palindrome")
    else: print("Not Palindrome")


s = input()
palindrome(s)