from to_do import TODO

# Refactoring
def task9(sentence, character):
    return character.lower() in sentence.lower()


if __name__ == "__main__":
    print(task9(sentence= "I code In KOTLIN", character= "i" ))


