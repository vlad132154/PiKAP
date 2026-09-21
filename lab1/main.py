import math


def discriminant(a, b, c):
    return b * b - 4 * a * c


def quadratic_roots(a, b, c):
    D = discriminant(a, b, c)
    if D < 0:
        return []
    if D == 0:
        return [-b / (2 * a)]
    sqrt_D = math.sqrt(D)
    return [(-b + sqrt_D) / (2 * a), (-b - sqrt_D) / (2 * a)]


def t_to_x(t):
    if t > 0:
        s = math.sqrt(t)
        return (s, -s)
    if t == 0:
        return (0,)
    return ()


def biquadratic_roots(a, b, c):
    if a == 0:
        return ()

    return tuple(sorted({
        x
        for t in quadratic_roots(a, b, c)
        for x in t_to_x(t)
    }))


def format_roots(roots):
    if not roots:
        return "Нет действительных корней"
    return "Корни: " + ", ".join(map(str, roots))


def main():
    a = float(input("Введите a: "))
    b = float(input("Введите b: "))
    c = float(input("Введите c: "))
    print(format_roots(biquadratic_roots(a, b, c)))


if __name__ == "__main__":
    main()