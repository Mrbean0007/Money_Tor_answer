
a = int(input('a:'))
b = int(input('b:'))


def main(a, b):

    if 1 <= a and b <= 10:
        rasto = a**b
        return rasto


print(main(a, b))
