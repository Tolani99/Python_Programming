import random

# Function to calculate the number of digits in a number
def num_length(n):
    no_len = 0
    while n > 0:
        no_len += 1
        n //= 10
    return no_len

# Karatsuba Multiplication Algorithm
def karatsuba_mult(x, y):
    # Base case: if the numbers are single-digit, perform simple multiplication
    if x < 10 or y < 10:
        return x * y
    
    # Find the number of digits in each number
    num1_length = num_length(x)
    num2_length = num_length(y)
    
    # Determine the maximum length and the half length
    max_num_length = max(num1_length, num2_length)
    half_max_num_length = (max_num_length // 2) + (max_num_length % 2)
    
    # Compute the divisors and remainders using the half length
    max_num_length_ten = 10 ** half_max_num_length
    a = x // max_num_length_ten
    b = x % max_num_length_ten
    c = y // max_num_length_ten
    d = y % max_num_length_ten
    
    # Recursively compute three products
    z0 = karatsuba_mult(a, c)
    z1 = karatsuba_mult(a + b, c + d)
    z2 = karatsuba_mult(b, d)
    
    # Use the three products to calculate the final result
    ans = (z0 * (10 ** (half_max_num_length * 2)) + 
           ((z1 - z0 - z2) * (10 ** half_max_num_length) + z2))
    
    return ans

if __name__ == "__main__":
    random.seed(0)
    MAX_VALUE = 10000
    
    # Test the Karatsuba multiplication algorithm with random integers
    for _ in range(MAX_VALUE):
        x = random.randint(0, MAX_VALUE)
        y = random.randint(0, MAX_VALUE)
        expected_product = x * y
        actual_product = karatsuba_mult(x, y)
        
        # Output the expected and actual products for comparison
        print("Expected:{} * {} = {}".format(x, y, expected_product))
        print("Actual: karatsuba_mult({},{}) = {}\n".format(x, y, actual_product))
        
        # Assertion to ensure the correctness of the implementation
        assert expected_product == actual_product

