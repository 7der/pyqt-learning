# Import all Modules
from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton , QVBoxLayout, QHBoxLayout , QGridLayout , QLineEdit ,QMessageBox
from PyQt5.QtGui import QFont  
import ui_popup_msgbox


class CalcApp(QWidget):

        def __init__(self, parent_widget):

            super().__init__(parent_widget)

            # Main App Objects and settings

            self.setWindowTitle("Password")
            self.setFixedSize(350, 400) # sets the size of the window to 400x200 pixels
            self.setWindowFlag(Qt.WindowType.CustomizeWindowHint, True)
            self.setWindowFlag(Qt.WindowType.WindowMinimizeButtonHint, False)
            self.setWindowFlag(Qt.WindowType.WindowMaximizeButtonHint, False)
        
            # Create all Objects/widgets here
            self.text_box = QLineEdit() # creates a text box for user input

            self.text_box.setReadOnly(True)
            self.text_box.setFont(QFont("Yu Gothic UI", 30)) # sets the font of the text box to Yu Gothic UI, size 14
            self.text_box.setStyleSheet("QLineEdit { background-color: #000000; color: white; }") 
            
            self.grid = QGridLayout() # creates a grid layout for the buttons
            self.buttons = ["7", "8", "9", 
                    "4", "5", "6", 
                    "1", "2", "3", 
                    "delete", "0", "Enter"]
            
            self.password = ""
            
            row = 0
            col = 0
            for text in self.buttons:
                button = QPushButton(text)
                button.clicked.connect(self.button_clicked)
                button.setStyleSheet("QPushButton { font: 25pt Yu Gothic UI; padding: 10 px; background-color: #000000; color: white; }") # sets the font of the buttons to Comic Sans Ms, size 14
                self.grid.addWidget(button, row, col)
                col += 1
                if col > 2:
                        col = 0
                        row += 1
                
          
            # Design you Layout, add your widgets to the screen

            master_layout = QVBoxLayout()
            master_layout.addWidget(self.text_box)
            master_layout.addLayout(self.grid)

            master_layout.setContentsMargins (10,10,10,10)

            # Set the final Layout to the Main window
            self.setLayout(master_layout) #sets the layout of the main window to the master layout

        def button_clicked(self):

                button = app.sender()
                text = button.text()
                
                if text == "Enter":
                        print("Entered Password:", self.password)
                        # symbol = self.text_box.text()
                        if self.password == "1234":
                                print("Access granted")
                                ui_popup_msgbox.show_info_msgbox(self, "Success", "Access Granted")
                        else:
                                print("Incorrect")
                                ui_popup_msgbox.show_warn_msgbox(self, "Warning", "Incorrect Password")
                        
                        self.password = ""
                        self.text_box.clear()

                elif text == "delete":
                        current_value = self.text_box.text()
                        self.text_box.setText(current_value[:-1])
                        self.password = self.password[:-1]
                        if self.password == "":
                                pass
                        else:
                                print(self.password)
                        
                        
                else:
                        self.password += text
                        self.text_box.setText("*" * len(self.password))
                        print(self.password)


        


            # Function



            # Events
        def show_warning_messagebox(self):
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText("Warning: Incorrect Password")
                msg.setWindowTitle("Warning Message Box")
                msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                retval = msg.exec()
                
        # def show_info_messagebox(self):
        #         msg = QMessageBox()
        #         msg.setIcon(QMessageBox.Warning)
        #         msg.setText("Warning")
        #         msg.setWindowTitle("Warning Message Box")
        #         msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        #         retval = msg.exec()
                





# Show and execute the app

if __name__ == "__main__":
        app = QApplication([]) # initializes the application
        main_window = CalcApp(None) # initializes the main window
        main_window.setStyleSheet("QWidget { background-color: #FFFFFF}")
        main_window.show()
        app.exec_()







