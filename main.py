from time import sleep
from fileRead.parser import CordParser
import re
import turtle

# All the options that the software provides.
options = ["View drawings", "Load from file", "Generate random drawings"]


def load_from_file():
    pattern = re.compile(r".+\.cord")
    print("Press Ctrl + c to go back to main menu.")
    print()

    try:
        while True:
            filename = input("Enter the .code file you want to run. : ")
            if re.match(pattern, filename):
                t = turtle.Turtle()
                with CordParser(filename, "r") as par:
                    sleep(1)
                    count = 0
                    for i in par:
                        if i[count][0] == "f":
                            t.fd(int(i[count][1]))
                        if i[count][0] == "b":
                            t.backward(int(i[count][1]))
                        if i[count][0] == "l":
                            t.left(int(i[count][1]))
                        if i[count][0] == "r":
                            t.right(int(i[count][1]))
                        if i[count][0] == "u":
                            t.penup()
                        if i[count][0] == "d":
                            t.pendown()

                        count += 1
                turtle.mainloop()
                break

            else:
                print("The file should be of type .code")

    except KeyboardInterrupt:
        start()


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