from PyQt5.QtWidgets import *

from software.ui_python.ui_generator_widget import Ui_GeneratorWidget

from software.app_data import AppData

class GeneratorWidget(QWidget):
    def __init__(self, app_data: AppData, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.app_data = app_data

        self.ui = Ui_GeneratorWidget()
        self.ui.setupUi(self)

        self.ui.generate_button.clicked.connect(self.generate_fruit_animal)

    def generate_fruit_animal(self):
        no_fruits = self.app_data.fruits.empty()
        no_animals = self.app_data.animals.empty()

        fruit = 'No Fruits' if no_fruits else self.app_data.fruits.random()
        animal = 'No Animals' if no_animals else self.app_data.animals.random()

        self.ui.fruit_label.setText(fruit)
        self.ui.animal_label.setText(animal)
