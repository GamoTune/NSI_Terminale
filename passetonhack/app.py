import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QTabWidget,
    QAction,
    QFileDialog,
    QTextEdit,
    QMessageBox,
    QBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QDialog,
)
import pickle
from hashlib import md5
import configparser
import os
import sys
from cryptography.fernet import Fernet


class NoteTakingApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.key = generate_or_read_key()

    def initUI(self):
        # Create a menu and toolbar for actions
        menu = self.menuBar()
        file_menu = menu.addMenu("File")

        open_note_action = QAction("Open Note", self)
        file_menu.addAction(open_note_action)

        # Create a tab widget to work with multiple notes
        self.tabs = QTabWidget(self)
        self.setCentralWidget(self.tabs)

        # Connect actions to functions
        open_note_action.triggered.connect(self.open_note)

    def open_note(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(
            self,
            "Open Note",
            "",
            "Note Files (*.notes);;All Files (*)",
            options=options,
        )
        if file_name:
            with open(file_name, "rb") as file:
                data = pickle.load(file)
                new_note_widget = QTextEdit()
                print(data)
                new_note_widget.setPlainText(data)
                self.tabs.addTab(new_note_widget, file_name)
                self.tabs.setCurrentWidget(new_note_widget)


    def open_note2(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(
            self, "Open Note", "", "Note Files (*.notes);;All Files (*)", options=options
        )
        if file_name:
            with open(file_name, "rb") as file:
                encrypted_data = pickle.load(file)
                decrypted_data = self.decrypt(encrypted_data, self.key)
                if decrypted_data is not None:
                    new_note_widget = QTextEdit()
                    new_note_widget.setPlainText(decrypted_data)
                    self.tabs.addTab(new_note_widget, file_name)
                    self.tabs.setCurrentWidget(new_note_widget)
                else:
                    QMessageBox.critical(
                        self,
                        "!! Erreur de déchiffrement !!",
                        "La clé de déchiffrement est incorrecte. \nLe fichier ne peut pas être déchiffré. \nVérifiez votre fichier config.cfg",
                        QMessageBox.Ok
                    )

    def decrypt(self, data, key):
        try:
            cipher_suite = Fernet(key)
            decrypted_data = cipher_suite.decrypt(data).decode()
            return decrypted_data
        except Exception as e:
            return None  # Retourne None si la clé est incorrecte


def generate_or_read_key():
    key = None
    if not os.path.exists("config.cfg"):
        pass
    else:
        # Configuration file exists, read the key
        key = read_key_from_config_file()
    return key


def read_key_from_config_file():
    config = configparser.ConfigParser()
    config.read("config.cfg")
    return config["Encryption"]["SecretKey"].encode()


def main():
    app = QApplication(sys.argv)
    ex = NoteTakingApp()
    ex.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()