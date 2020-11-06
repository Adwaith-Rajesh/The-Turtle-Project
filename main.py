from time import sleep
from fileRead.parser import CordParser
from static.complicated import *
from static.simple import *
from generator.rand_gen import RandomArt
import re
import turtle
import tkinter

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

    preloads = [
        "flowers", "modern art", "polygon", "color gamut", "protractor",
        "color spiral", "wormhole", "spider web"
    ]

    try:
        print("Press Ctrl + C to go back to mani menu.")

        while True:
            print("Choose a style from the option. ")
            for i, op in enumerate(preloads):
                print(f"{i + 1}) {op}")

            try:
                option = int(input(""))
                if 0 < option <= len(preloads):
                    turtle.reset()
                    if option == 1:
                        t = turtle.Turtle()
                        flowers(t)
                        turtle.done()

                    if option == 2:
                        t = turtle.Turtle()
                        modern_art(t)
                        turtle.done()

                    if option == 3:
                        t = turtle.Turtle()
                        polygon(t)
                        turtle.done()

                    if option == 4:
                        t = turtle.Turtle()
                        color_gamut(t)
                        turtle.done()

                    if option == 5:
                        t = turtle.Turtle()
                        protractor(t)
                        turtle.done()

                    if option == 6:
                        t = turtle.Turtle()
                        color_spiral(t)
                        turtle.done()

                    if option == 7:
                        t = turtle.Turtle()
                        wormhole(t)
                        turtle.done()

                    if option == 8:
                        t = turtle.Turtle()
                        spider_web(t)
                        turtle.done()
                else:
                    raise ValueError

            except ValueError:
                print("Enter a valid option.")
            except turtle.Terminator:
                pass

            except tkinter.TclError:
                pass

    except KeyboardInterrupt:
        start()


def generate_random_drawings():
    try:
        t = turtle.Turtle()
        ra = RandomArt(t)
        ra.start()
        turtle.mainloop()
    except:
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