import os
import random

DATA_DIR_PATH = 'data'
FRUITS_FILE_PATH = f'{DATA_DIR_PATH}/fruits.txt'
ANIMALS_FILE_PATH = f'{DATA_DIR_PATH}/animals.txt'

class FileBackedSet:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.data = set()

        os.makedirs(DATA_DIR_PATH, exist_ok=True)

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
