import re

from to_do import TODO
import re


def task10(password):
    has_lowercase = len(re.findall("[a-z]", password)) > 0
    has_special_character = len(re.findall("[$#@]", password)) > 0
    has_uppercase = len(re.findall("[A-Z]", password)) > 0
    has_number = len(re.findall("[0-9]", password)) > 0
    has_correct_length = len(password) in range(6, 11)

    return has_lowercase and has_special_character and has_uppercase and has_number and has_correct_length


if __name__ == "__main__":
    print(task10(password="San$991"))
