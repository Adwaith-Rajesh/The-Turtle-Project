options = ["View drawings", "Load from file", "Generate random drawings"]


def load_option(op):
    if op == 1:
        pass  # load the list of premeade drawings

    elif op == 2:
        pass  # ask the user for the file

    elif op == 3:
        pass  # Show the user a randomly generated drawing with option to save

    else:
        print("The option is not valid")
        start()


def start():

    print("Choose an option")

    for index, op in enumerate(options):
        print(f"{index + 1}) {op}")

    option = input()
    load_option(int(option))


if __name__ == "__main__":
    print("Welcome to The Turtle Project")
    start()