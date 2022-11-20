

class Board:
    # returns the read input file
    @staticmethod
    def read_input_file():
        f = open("sample-input.txt", "r")
        return f

    # returns a list of the different boards
    def list_of_boards(self):
        list_of_boards = []
        lines = self.read_input_file()
        for line in lines:
            if "#" not in line:
                if not line.isspace():
                    list_of_boards.append(line[0:len(line)-1])
        return list_of_boards
