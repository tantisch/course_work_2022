import matplotlib.pyplot as plt
import numpy as np

eps = 0.0001

global coefs
coefs = [1, 2, -8, -16, 11, 28, 12]  # Коефіцієнти многочлена

f = np.poly1d(coefs)


def equation_in_str(coefs):
    s = ''
    for pow, coef in enumerate(coefs[::-1][:-1]):
        s += f'{coef}*x^{pow} + '

    s += f'{coefs[0]}*x^{len(coefs) - 1}'

    return s


def diff_(f):
    return np.polyder(f)


def check_if_unimodal(f, a, b):
    F = diff_(f)
    roots = np.roots(F)
    good_x = [x for x in roots if a < x < b]
    if len(good_x) != 1:
        return False
    return True