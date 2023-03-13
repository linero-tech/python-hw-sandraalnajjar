from to_do import TODO


def task6(number):

    result = 0
    while number > 0:
        i = number % 10
        number = number // 10
        result = (result * 10) + i


    return result


if __name__ == "__main__":
    print(task6(678))
