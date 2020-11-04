from pathlib import Path
from time import sleep


# hold the headers for all the ANSI codes
class Bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RESET = '\u001b[0m'


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
            print(f"{index + 1}) {Bcolors.BOLD}{op}")
            print(Bcolors.RESET)

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
            print(f"{Bcolors.WARNING}Enter a valid option. \n")
            print(Bcolors.RESET)
            sleep(1)


if __name__ == "__main__":
    print(f"{Bcolors.OKCYAN}Welcome to The Turtle Project")
    print(Bcolors.RESET)

    try:
        print("Press Ctrl+C to exit")
        start()

    except KeyboardInterrupt:
        print(f"{Bcolors.OKBLUE}Exiting, Thanks for using.")
        print()
        print(Bcolors.RESET)