from to_do import TODO

# Refactoring
def task10_1(assessments):
    return len(assessments)




def task10_2(assessments):
    return assessments[3]


def task10_3(assessments):
    return assessments[len(assessments) // 2]


def task10_4(assessments):
    return assessments[0:3]

if __name__ == "__main__":
    print(task10_1(assessments="LMHHF"))
    print(task10_2(assessments="LMFHMF"))
    print(task10_3(assessments="LMFHM"))
    print(task10_4(assessments="LMFHM"))
