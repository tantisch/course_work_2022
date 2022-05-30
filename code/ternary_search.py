def ternary_search(f, a, b, eps, min_max):
    while abs(b - a) >= eps:
        left_t = a + (b - a) / 3
        right_t = b - (b - a) / 3

        if min_max == 'max':
            if f(left_t) > f(right_t):
                b = right_t
            else:
                a = left_t
        else:
            if f(left_t) <= f(right_t):
                b = right_t
            else:
                a = left_t

    # maximum is between current bounds
    ans = (b + a) / 2
    return round(ans, 2), round(f(ans), 2)