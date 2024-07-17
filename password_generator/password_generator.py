import random
import string

def generate_password(length, use_upper=True, use_lower=True, use_digits=True, use_special=True):
    length = int(input("Enter the length of required password: "))
    if length < 4:
        raise ValueError("Password length should be at least 4 characters.")

    char_pools = []
    if use_upper:
        char_pools.append(string.ascii_uppercase)
    if use_lower:
        char_pools.append(string.ascii_lowercase)
    if use_digits:
        char_pools.append(string.digits)
    if use_special:
        char_pools.append(string.punctuation)
    if not char_pools:
        raise ValueError("At least one character set must be selected.")

    password = [random.choice(pool) for pool in char_pools]
    all_chars = ''.join(char_pools)
    password += random.choices(all_chars, k=length - len(password))
    random.shuffle(password)
    return ''.join(password)

if __name__ == "__main__":
    print("Generated Password:",
          generate_password(length=12, use_upper=True, use_lower=True, use_digits=True, use_special=True))
