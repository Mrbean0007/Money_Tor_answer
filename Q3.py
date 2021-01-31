n1 = 0
n2 = 1
out = []
count = 0
fibo_no = int(input('a:'))


def main(n1, n2, count, fibo_no):
    if 1 <= fibo_no <= 1000000:
        while count <= fibo_no:
            out.append(n1)
            fib = n1+n2
            n1 = n2
            n2 = fib
            count += 1


main(n1, n2, count, fibo_no)
print(out)
