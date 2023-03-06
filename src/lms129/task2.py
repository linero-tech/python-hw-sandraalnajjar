from to_do import TODO


def task2(number):

    result = True

    if number > 1:
        for i in range(2,number+1):
            if (number % i) == 0:
                print(False)
            


    return result


if __name__ == "__main__":
    print(task2(5))
