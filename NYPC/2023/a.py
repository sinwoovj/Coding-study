import random

def generate_random_binary(length):
    binary_string = ''.join(random.choice(['0', '1']) for _ in range(length))
    return binary_string

length = 1000000
random_binary = generate_random_binary(length)
print(random_binary)
