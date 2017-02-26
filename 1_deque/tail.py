from collections import deque
from pprint import pprint


def tail_deque(filename, n=10):
    """
    retorna as ultimas linhas de um arquivo

    fonte: https://docs.python.org/3/library/collections.html
    """
    with open(filename) as f:
        return deque(f, n)


def tail_list(filename, n=10):
    """
    retorna as primeiras linhas de um arquivo
    """
    with open(filename) as f:
        return f.readlines()[-n:]


pprint(tail_deque('tabacaria.txt'))
pprint(tail_list('tabacaria.txt'))
