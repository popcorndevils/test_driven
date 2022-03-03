def is_multiple(value, mod):
    return value % mod == 0

def fizzbuzz(value):
    if is_multiple(value, 3):
        if is_multiple(value, 5):
            return "fizzbuzz"
        return "fizz"
    elif is_multiple(value, 5):
        return "buzz"
    return str(value)
