from collections import deque
from pprint import pprint


def tail(filename, n=10):
    """
    retorna as ultimas linhas de um arquivo

    fonte: https://docs.python.org/3/library/collections.html
    """
    with open(filename) as f:
        return deque(f, n)


pprint(tail('tabacaria.txt', 6))
