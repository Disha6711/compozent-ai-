def is_palindrome():
    s = input("Enter a string to check if it's a palindrome: ")

    s = s.replace(" ", "").lower()
    
    if s == s[::-1]:
        print("The given string is a palindrome.")
    else:
        print("The given string is not a palindrome.")

is_palindrome()
