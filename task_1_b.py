def is_palindrome():
    # Take input from the user
    s = input("Enter a string to check if it's a palindrome: ")
    
    # Remove spaces and convert to lowercase
    s = s.replace(" ", "").lower()
    
    # Check if the string is equal to its reverse
    if s == s[::-1]:
        print("The given string is a palindrome.")
    else:
        print("The given string is not a palindrome.")

# Call the function
is_palindrome()
