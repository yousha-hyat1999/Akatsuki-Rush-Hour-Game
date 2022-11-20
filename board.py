

class Board:
    @staticmethod
    def read_input_file():
        f = open("sample-input.txt", "r")
        return f

    def list_of_boards(self):
        list_of_boards = []
        lines = self.read_input_file()
        for line in lines:
            if "#" not in line:
                if not line.isspace():

                    list_of_boards.append(line)
        print(list_of_boards)
