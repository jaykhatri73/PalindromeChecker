def is_palindrome(x):

    # making user input lowercase
    x = x.lower()

    reversed_x = x[::-1]

    if x == reversed_x:
        return True
    else:
        return False


user_input = input("Enter a word: ")
if is_palindrome(user_input):
    print("It's a palindrome!")
else:
    print("It's not a palindrome.")
