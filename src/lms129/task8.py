from to_do import TODO


def task8(number):
    result = 0

    if number > 0:
        for i in str(number):
            result += int(i)

    return result


if __name__ == "__main__":
    print(task8(123))
