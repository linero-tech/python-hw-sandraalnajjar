from to_do import TODO


def task3(number):
    result = 1
    if number > 0:
        for i in range(1, number+1):
            result *= i

    return result


if __name__ == "__main__":
    print(task3(5))



