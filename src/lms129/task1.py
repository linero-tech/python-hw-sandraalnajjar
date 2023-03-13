from to_do import TODO


# Refactoring:
def task1(a, b):
    result = 0
    if a < b:
        for i in range(a, b + 1):
            result += i

    return result

if __name__ == "__main__":
    print(task1(1, 5))
    print(task1(3, 3))

