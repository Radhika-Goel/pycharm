#! /usr/local/bin/python3
import random
import time


def testing():
    search = True
    while search:
        m, n = random.randint(0, 1 + (10 ** 18)), random.randint(0, 1 + (10 ** 18))
        if m > n:
            search = True
        else:
            search = False

    return m, n


def naiveAlgorithm(values):
    from_, to = values
    result = 0

    current = 0
    next_value = 1

    for i in range(to + 1):
        if i >= from_:
            result += current

        current, next_value = next_value, current + next_value

    return result % 10


def efficientAlgorithm(values):
    m, n = values
    m += 1
    n += 1

    k, a, b, addition = 1, 0, 1, 0

    while k <= n:
        a, b = (b, (a + b) % 10) if k > 2 else (a, b)
        if k >= m:
            addition += (b if k > 2 else (a if k == 1 else (b if k == 2 else 0)))
        k += 1
    return addition % 10 if n != 1 else a


tests = 0
counter = 100
runtime_naive, runtime_efficient = 0, 0

while tests < counter:
    test = testing()

    start_time = time.time()
    naive = naiveAlgorithm(test)
    runtime_naive += (time.time() - start_time)

    start_time = time.time()
    efficient = efficientAlgorithm(test)
    runtime_efficient += (time.time() - start_time)

    if (efficient != naive):
        print("\nFor n = {}, results don't match: {} vs {}".format(test, naive, efficient))
        break
    else:
        print("\nResult for input {} : {}".format(test, efficient))
        tests += 1

# print("\nNaive Total Runtime: {}".format(runtime_naive))
# print("Efficient Total Runtime: {}".format(runtime_efficient))
print("\nEfficient Algorithm is  x{0:.2f} faster".format(runtime_naive / runtime_efficient))