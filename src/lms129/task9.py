from to_do import TODO


def task9(temperature):
    magnitude= 50
    unit = "F"
    temperature= 50f


    result = str(int((temperature[-1].upper()) == (temperature * 9 / 5) + 32)) + "C"

    if temperature[-1].upper() == "C":
        result = str(int((temperature[-1].upper()) / 5 == (temperature - 32) / 9)) + "F"

    return result


if __name__ == "__main__":
    print(task9(temperature is 50F))
