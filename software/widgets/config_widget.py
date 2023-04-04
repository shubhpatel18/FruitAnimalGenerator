from PyQt5.QtWidgets import *

from software.ui_python.ui_config_widget import Ui_ConfigWidget

from software.app_data import AppData, FileBackedSet

class ListManipulator:
    def __init__(self, list_widget: QListWidget, entry: QLineEdit, add_button: QPushButton, del_button: QPushButton, data: FileBackedSet):
        self.list_widget = list_widget
        self.entry = entry
        self.add_button = add_button
        self.del_button = del_button
        self.data = data

        self.entry.returnPressed.connect(self._add_to_list)

        self.add_button.clicked.connect(self._add_to_list)
        self.del_button.clicked.connect(self._remove_from_list)

        self._load_list()

    def _load_list(self):
        self.list_widget.clear()
        self.list_widget.addItems(sorted(self.data.get()))

    def _add_to_list(self):
        if self._red_if_empty(self.entry):
            return

        datum = self.entry.text()
        self.data.add(datum)
        self.entry.clear()
        self._load_list()

    def _remove_from_list(self):
        selected_items = self.list_widget.selectedItems()
        if not selected_items:
            return

        prev_selected_row = self.list_widget.currentRow()

        datum = selected_items[0].text()
        self.data.remove(datum)
        self._load_list()

        self.list_widget.setCurrentRow(prev_selected_row)

    def _red_if_empty(self, line_edit: QLineEdit):
        if line_edit.text():
            line_edit.setStyleSheet("")
            return False
        else:
            line_edit.setStyleSheet("background-color: #ff6060")
            return True

class ConfigWidget(QWidget):
    def __init__(self, app_data: AppData, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.app_data = app_data

        self.ui = Ui_ConfigWidget()
        self.ui.setupUi(self)

        self.fruit_manipulator = ListManipulator(
            self.ui.fruit_list,
            self.ui.fruit_entry,
            self.ui.fruit_add,
            self.ui.fruit_del,
            self.app_data.fruits
        )

        self.animal_manipulator = ListManipulator(
            self.ui.animal_list,
            self.ui.animal_entry,
            self.ui.animal_add,
            self.ui.animal_del,
            self.app_data.animals
        )
