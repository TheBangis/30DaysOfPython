''' 30 Days of Python - Day 12
Exercise 1: level 1--------------- Modules'''

from random import random, randint
import string
import random

# Number 1
def random_user_id():
    return ''.join(str(random.choice(string.ascii_letters + string.digits)) for i in range(6))
print(random_user_id())

# Number 2
def user_id_gen_by_user():
    num_char = int(input("number of characters: "))
    num_id = int(input("number of id: "))
    return [''.join(str(random.choice(string.ascii_letters + string.digits)) for i in range(num_char)) for x in range(num_id)]
print(user_id_gen_by_user())

# Number 3
def rgb_color_gen():
    return 'rgb('+ ','.join(str(randint(1, 255)) for i in range(3)) + ')'
print(rgb_color_gen())

