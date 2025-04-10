import random
import string

def generate_short_link(length: int = 4):

    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))