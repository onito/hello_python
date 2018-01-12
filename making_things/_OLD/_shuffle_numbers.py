import random

def get_secret_num_digit(num_digits=10):
    """ Return certain digits of number_str, num_digits = less than 10 digits
    Returns a string that is numDigits long, made up of unique random digits.
    """
    numbers = list(range(10))
    # print('neated numbers=',numbers)
    random.shuffle(numbers)
    print('shuff_numbers =', numbers)

    secret_number = ''
    for n in range(num_digits):
        secret_number += str(numbers[n])
    return secret_number

print(get_secret_num_digit.__doc__)
rand_num_arr = []

for i, num in enumerate(range(10), 1):
    rand_num = get_secret_num_digit(5)
    rand_num_arr.append(rand_num)

for i, num in enumerate(rand_num_arr, 1):
    print('%s = %s'% (i, num))

print(rand_num_arr)
