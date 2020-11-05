from time import sleep

# All the options that the software provides.
options = ["View drawings", "Load from file", "Generate random drawings"]


def load_from_file():
    pass


def load_preload_drawings():
    pass


def generate_random_drawings():
    pass


def start():

    while True:

        print("Choose an option")
        print()

        for index, op in enumerate(options):
            print(f"{index + 1}) {op}")

        print()
        try:
            op = int(input(""))

            if op == 1:
                load_preload_drawings()
                break

            elif op == 2:
                load_from_file()
                break

            elif op == 3:
                generate_random_drawings()
                break

        except ValueError:
            print(f"Enter a valid option. \n")
            sleep(1)


if __name__ == "__main__":
    print(f"Welcome to The Turtle Project")

    try:
        print("Press Ctrl+C to exit")
        start()

    except KeyboardInterrupt:
        print(f"Exiting, Thanks for using.")
        print()