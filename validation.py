

def validName():
    name = input("Enter a name: ")
    if not name.isalpha():
        print("Wrong name")
        raise ValueError("Value consist not only letters")

    return name

try:
    validName()
except ValueError as e:
    print("Wrong value type", e)
finally:
    print("DONE")
