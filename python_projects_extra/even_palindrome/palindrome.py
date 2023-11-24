def create_even_palindrome(base_string):
    return base_string + base_string[::-1]

base_string = "abcd"
even_palindrome = create_even_palindrome(base_string)

print(even_palindrome)

