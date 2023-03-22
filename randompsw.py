import random
import string

def generate_password(length):
    # Generate a random password of specified length
    password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(length))
    return password

# Generate a password of length 12
print(generate_password(12))
