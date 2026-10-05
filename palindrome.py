def is_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        if not s[left].isalnum():        # skip spaces/punctuation on the left
            left += 1
        elif not s[right].isalnum():     # skip spaces/punctuation on the right
            right -= 1
        elif s[left].lower() != s[right].lower():
            return False                 # mismatch -> not a palindrome
        else:
            left += 1
            right -= 1
    return True


text = input("Enter a sentence: ")
print("Palindrome" if is_palindrome(text) else "Not a palindrome")