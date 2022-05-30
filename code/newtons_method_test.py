from newtons_method import *

fig = plt.figure(figsize=(12, 10))

all_extremum = []

for guess in np.linspace(-20, 20, 50):
    ext = round(newton(f, guess, eps, 50), 2) # find extremum value nearest to guess
    if ext and ext not in map(lambda x: x[0], all_extremum):
        all_extremum.append([ext, round(f(ext), 2)])

print(all_extremum)

x = np.linspace(-4, 4, 100)
y = f(x)

str_eq = equation_in_str(coefs)

for p in all_extremum:
    plt.plot(*p, marker='o', color='r')
    plt.text(p[0], p[1] + 1, f'({p[0]}, {p[1]})', horizontalalignment='center')

plt.title('y = ' + str_eq)
plt.ylim(-30, 100)
plt.grid()
plt.plot(x, y)
plt.show()