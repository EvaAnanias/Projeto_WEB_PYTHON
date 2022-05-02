# from inspect import signature
from random import randint

from faker import Faker

# from unicodedata import category


def rand_ratio():
    return randint(840, 900), randint(473, 573)


fake = Faker('pt_BR')
# print(signature(fake.random_number))


def make_calendario():
    return {

        'nome': fake.sentence(nb_words=6),
        'data': fake.random_number(digits=4, fix_len=True),
        'local': fake.sentence(nb_words=8),
        'hora_inicio': fake.random_number(digits=4, fix_len=True),
        'hora_inicio_unit': 'Minutos',
        'hora_termino': fake.random_number(digits=4, fix_len=True),
        'hora_termino_unit': 'Minutos',
        'observação': fake.sentence(nb_words=80),
        #    'author': {
        #       'first_name': fake.firsh_name(),
        #      'last_name': fake.firsh_name(),
        #   },
        #   'category': {
        #       'name': fake.word()
        #   }
    }


if __name__ == '__main__':
    from pprint import pprint
    pprint(make_calendario())
