# import random, string
# x = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
# print(x)

import random, string
# x = ''.join(random.choice(string.ascii_uppercase  + string.digits) for _ in range(8))
# print(x)

def order_no(x):
    x = ''.join(random.choice(string.ascii_uppercase  + string.digits) for _ in range(8))
    print(x)
    return x

order_no(x)