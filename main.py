
options = [
    "View drawings",
    "Load from file",
    "Generate random drawings"
]


def load_option(op):
    if op == 5:
        start()

def start():
    
    print("Choose an option")

    for index , op in enumerate(options):
        print(f"{index + 1}) {op}")

    option = input()
    load_option(int(option))



if __name__ == "__main__":
    print("Welcome to The Turtle Project")
    start()