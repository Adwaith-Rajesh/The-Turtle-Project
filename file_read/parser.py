class CordParser:
    """
    the file should end in .cord, and should contains the direction and the angles to turn.
    f -> forward
    b -> backward
    r -> right
    l -> left
    u -> stop drawing
    p -> start drawing

    The file should be written as:

    f=100
    r=20
    b=50
    ..etc
    """
    def __init__(self, filename: str, method: str) -> None:
        self.valid_chrs = ["f", "b", "r", "l", "u", "d"]
        if not filename.endswith(".cord"):
            raise TypeError("Filename should end with \".cord\"")
        self.file_ = open(filename, method)
        self.file_data = self.file_.read().split("\n")

    def __enter__(self):
        rl = []
        for i, d in enumerate(self.file_data):
            nd = d.replace(" ", "").split("=")
            if nd[0] not in self.valid_chrs:
                raise TypeError("Invalid character found")
            rl.append({i: nd})
        return self.data(rl)

    def __exit__(self, type, value, traceback):
        self.file_.close()

    @staticmethod
    def data(list_):
        yield from list_
