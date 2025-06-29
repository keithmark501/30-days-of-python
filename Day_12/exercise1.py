import random
import string

def random_user_id():
    characters = string.ascii_letters + string.digits  
    user_id = ''.join(random.choices(characters, k=6))
    return user_id

print(random_user_id())  

def user_id_gen_by_user():
    num_chars = int(input("Enter number of characters per ID: "))
    num_ids = int(input("Enter number of IDs to generate: "))
    characters = string.ascii_letters + string.digits

    for _ in range(num_ids):
        user_id = ''.join(random.choices(characters, k=num_chars))
        print(user_id)

def rgb_color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"rgb({r},{g},{b})"

print(rgb_color_gen()) 

import random

def list_of_hexa_colors(n):
    colors = []
    for _ in range(n):
        hex_color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        colors.append(hex_color)
    return colors

def list_of_rgb_colors(n):
    colors = []
    for _ in range(n):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        colors.append(f"rgb({r},{g},{b})")
    return colors

def generate_colors(color_type, num=1):
    if color_type.lower() == 'hexa':
        return list_of_hexa_colors(num)
    elif color_type.lower() == 'rgb':
        return list_of_rgb_colors(num)
    else:
        return "Invalid color type. Use 'hexa' or 'rgb'."

import random

def shuffle_list(input_list):
    shuffled = input_list[:]
    random.shuffle(shuffled)
    return shuffled

def unique_random_numbers():
    return random.sample(range(10), 7)