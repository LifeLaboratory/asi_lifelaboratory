def gentext(length):
    import random
    return ''.join([chr(random.randint(65, 90)) if random.randint(0, 1) else chr(random.randint(97, 122)) for _ in range(length)])
