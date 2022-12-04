import csv
from os.path import exists


class ExcelFile:
    def __init__(self):
        file_exists = exists('Solution.csv')
        if file_exists:
            self.file = open('Solution.csv', 'a', newline='')
            self.header = ['Puzzle Number', 'Algorithm', 'Heuristic', 'Length of the Solution',
                           'Length of the Search Path',
                           'Execution Time (in seconds)']
            return
        else:
            self.file = open('Solution.csv', 'w', newline='')
            self.time = ''
            self.search_path_length = ''
            self.heuristic = ''
            self.algorithm = ''
            self.puzzle_number = ''
            self.solution_length = ''
            with self.file:
                self.header = ['Puzzle Number', 'Algorithm', 'Heuristic', 'Length of the Solution',
                               'Length of the Search Path',
                               'Execution Time (in seconds)']
                writer = csv.DictWriter(self.file, fieldnames=self.header)
                writer.writeheader()

    def set_puzzle_number(self, puzzle_number):
        self.puzzle_number = puzzle_number

    def set_algorithm(self, algorithm):
        self.algorithm = algorithm

    def set_heuristic(self, heuristic):
        self.heuristic = heuristic

    def set_search_path_length(self, search_path_length):
        self.search_path_length = search_path_length

    def set_solution_length(self, solution_length):
        self.solution_length = solution_length

    def set_time(self, time):
        self.time = time

    def write_row(self):
        self.file = open('Solution.csv', 'a', newline='')
        with self.file:
            self.header = ['Puzzle Number', 'Algorithm', 'Heuristic', 'Length of the Solution',
                           'Length of the Search Path',
                           'Execution Time (in seconds)']
            writer = csv.DictWriter(self.file, fieldnames=self.header)
            writer.writerow({'Puzzle Number': self.puzzle_number,
                             'Algorithm': self.algorithm,
                             'Heuristic': self.heuristic,
                             'Length of the Solution': self.solution_length,
                             'Length of the Search Path': self.search_path_length,
                             'Execution Time (in seconds)': self.time
                             })

    def clear_state(self):
        self.time = ''
        self.search_path_length = ''
        self.heuristic = ''
        self.algorithm = ''
        self.puzzle_number = ''
        self.solution_length = ''

    def close_file(self):
        self.file.close()
