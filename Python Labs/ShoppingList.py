from PySide2.QtWidgets import QApplication, QMainWindow, QGridLayout, QLineEdit, QPushButton, QWidget, QListWidget, QAbstractItemView, QDialogButtonBox, QDialog, QLabel
from PySide2.QtCore import QSize
import sys
import os

ITEMS_FILE = "Items.txt"

class ConfirmRemoveDialoge(QDialog):
    def __init__(self, main_window):
        """Initiazes QDialog object
        """
        super().__init__()
        self.setWindowTitle("Warning")
        self.main_window = main_window

        warning_text = QLabel("Are you sure you want to delete the items selected?")
        confirm_button = QDialogButtonBox(QDialogButtonBox.Ok)
        cancel_button = QDialogButtonBox(QDialogButtonBox.Cancel)

        confirm_button.accepted.connect(self.confirm_removal)
        confirm_button.accepted.connect(self.accept)

        cancel_button.rejected.connect(self.reject)

        layout = QGridLayout()
        layout.addWidget(warning_text, 0, 0)
        layout.addWidget(confirm_button, 1, 0)
        layout.addWidget(cancel_button, 1, 1)

        self.setLayout(layout)
    
    def confirm_removal(self):
        """Removes items from Items.txt file and the QListWidget after confirmation
        """
        items_selected = self.main_window.get_shopping_list().selectedItems()
        for item in items_selected:
            self.main_window.get_shopping_list().takeItem(self.main_window.get_shopping_list().row(item))
        self.main_window.save_items()

class MainWindow(QMainWindow):
    def __init__(self):
        """Initializes QMainWindow object
        """
        super().__init__()
        self.setWindowTitle("Shopping List")
        self.setMinimumSize(QSize(335, 600))

        self.text_input = QLineEdit()
        self.shopping_list = QListWidget()
        self.items_saved = []

        add_item_button = QPushButton()
        remove_item_button = QPushButton()
        container = QWidget()
        layout = QGridLayout()

        add_item_button.setText("Add Item")
        remove_item_button.setText("Remove Item(s)")
        add_item_button.clicked.connect(self.add_button_clicked)
        self.text_input.returnPressed.connect(self.add_button_clicked)
        remove_item_button.clicked.connect(self.remove_button_clicked)
        
        self.shopping_list.setSortingEnabled(True)
        self.shopping_list.setSelectionMode(QAbstractItemView.MultiSelection)

        layout.addWidget(self.text_input, 0, 0)
        layout.addWidget(add_item_button, 0, 1)
        layout.addWidget(self.shopping_list, 1, 0, 1, 2)
        layout.addWidget(remove_item_button, 2, 0, 2, 2)

        container.setLayout(layout)
        self.setCentralWidget(container)

        self.load_data()
    
    def add_button_clicked(self):
        """Adds items to the Items.txt file and QListWidget
        """
        item_to_add = self.text_input.text()
        if len(item_to_add) > 0:
            self.shopping_list.addItem(item_to_add)
        self.text_input.setText("")
        self.text_input.setFocus()
        self.save_items()
    
    def get_shopping_list(self):
        """Returns QListWidget object
        """
        return self.shopping_list
        
    def remove_button_clicked(self):
        """Calls dialog for confirmation after wanting to delete
        """
        dialog = ConfirmRemoveDialoge(self)
        dialog.exec_()
    
    def save_items(self):
        """Saves items in the file Items.txt
        """
        curr_row = 0
        self.items_saved = []
        while self.shopping_list.item(curr_row) != None:
            self.items_saved.append(self.shopping_list.item(curr_row).text())
            curr_row += 1
        file = open(get_file_path(), 'w')
        for item in self.items_saved:
            file.write(item + "\n")
        file.close()
    
    def load_data(self):
        """Loads the data in Items.txt after the application starts running
        """
        file = open(get_file_path(), 'r')
        data = file.readlines()

        for item in data:
            item = item[:-1]    #Omits the \n character
            if len(item) > 0:
                self.shopping_list.addItem(item)
        file.close()

def get_file_path():
    """Gets file path of Items.txt
    """
    for dir_name, sub_names, file_names in os.walk(os.getcwd()):
        if ITEMS_FILE in file_names:
            FILE_PATH = dir_name + "/" + ITEMS_FILE
            return FILE_PATH
    else:
        for dir_name, sub_names, file_names in os.walk(os.getcwd()):
            if "ShoppingList.py" in file_names:
                file = open(dir_name + "/" + ITEMS_FILE, 'w')
                file.close()
                return dir_name + "/" + ITEMS_FILE

app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
app.exec_()