from to_do import TODO


def task7(a, b):

    result = a ** b

    if a == 0 and b == 0:
        result = 1
        for i in str(b):
            result += int (a)

    return result


if __name__ == "__main__":
    print(task7(a=2, b=3))
