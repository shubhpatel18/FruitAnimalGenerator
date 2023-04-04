import random

FRUITS_FILE_PATH = 'software/data/fruits.txt'
ANIMALS_FILE_PATH = 'software/data/animals.txt'

class FileBackedSet:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.data = set()

        try:
            with open(self.file_path, 'r') as file:
                for line in file:
                    self.data.add(line.rstrip())
        except (IOError, FileNotFoundError):
            pass

    def get(self):
        return set(self.data)

    def add(self, datum):
        self.data.add(datum)
        self._write()

    def remove(self, datum):
        self.data.remove(datum)
        self._write()

    def random(self):
        return random.choice(tuple(self.data))

    def empty(self):
        return not self.data

    def _write(self):
        try:
            with open(self.file_path, 'w') as file:
                for datum in self.data:
                    file.write(f'{datum}\n')
        except (IOError, FileNotFoundError):
            pass

class AppData:
    def __init__(self):
        self.fruits = FileBackedSet(FRUITS_FILE_PATH)
        self.animals = FileBackedSet(ANIMALS_FILE_PATH)
