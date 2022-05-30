from function import *
from ternary_search import ternary_search

x = np.linspace(-4, 4, 100)
y = f(x)

a = -1.3
b = 0.5
min_max = 'min'

if check_if_unimodal(f, a, b):
    ext = ternary_search(f, a, b, eps, min_max)
    print(f'Find {min_max} using ternary search method from {a} to {b}')

    fig = plt.figure(figsize=(11, 9))

    plt.plot(x, y)
    plt.plot(*ext, marker='o', color='r')  # plot extremum
    plt.plot(a, f(a), marker='<', color='g', markeredgewidth=4)  # plot left border (a)
    plt.plot(b, f(b), marker='>', color='g', markeredgewidth=4)  # plot right border (b)

    plt.text(ext[0], ext[1] + 1, f'({ext[0]}, {ext[1]})', horizontalalignment='center')
    plt.text(a, f(a) - 3.5, 'a', horizontalalignment='center')
    plt.text(b, f(b) - 3.5, 'b', horizontalalignment='center')

    plt.title('y = ' + equation_in_str(coefs))
    plt.ylim(-30, 100)
    plt.grid()
    plt.show()
    print('NOTE: if you dont see the red point(extremum) you have to change min_max value')
else:
    print(f'This function from {a} to {b} is not unimodal. Please change the range')