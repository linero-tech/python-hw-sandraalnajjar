from to_do import TODO


def task4():
    result = 0
    for i in range(1, 1000):
        if i % 9 == 0:
            result += i
    return result


if __name__ == "__main__":
    print(task4())
