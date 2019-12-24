#!python3
# -*-encoding:utf8-*-

import random
import string


def get_random_name():
    return ''.join([random.choice(string.ascii_uppercase)
        for i in range(8)])


def get_file_name():
    exist = set()
    file_name = None
    while True:
        previous = yield file_name
        file_parts = previous.split('.')
        extension = file_parts[-1]
        file_name = f'{get_random_name()}.{extension}'
        while file_name in exist:
            file_name = f'{get_random_name()}.{extension}'
        exist.add(file_name)


if __name__ == '__main__':
    generator = get_file_name()
    next(generator)
    form = '.jpg'
    names = generator.send(get_random_name() + form)
    with open('car' + form) as f:
        print(names)
