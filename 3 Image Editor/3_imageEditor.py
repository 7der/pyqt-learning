# Import Modules
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton , QVBoxLayout, QHBoxLayout , QComboBox , QListWidget # type: ignore
from PyQt5.QtCore import Qt # type: ignore
from PIL import Image, ImageFilter, ImageEnhance
from pathlib import Path

folder = Path("3 Image Editor")

class Editor():

    def __init__(self):
        
        # Main App Objects and settings
        app = QApplication([])

        # main_window = QWidget()
        self.setWindowTitle("Image Editor")
        self.setFixedSize(900, 700) # sets the size of the window to 400x200 pixels

        # 
        self.pic = None
        self.original_pic = None
        self.file = None
        self.save_folder = "edits/"
                
        blank_list = []
        # files = [f for f in folder.iterdir() if f.is_file()]
        # # print(files)


        # Create all Objects/widgets
        btn_folder = QPushButton("Select Folder")
        list_file= QListWidget()

        # buttons = ["Left", "Right", "Mirror", "Sharpness", "B/W", "Color", "Contrast"]
                
        btn_left= QPushButton("Left")
        btn_right = QPushButton("Right")
        btn_mirror = QPushButton("Mirror")
        btn_sharpness = QPushButton("Sharpness")
        btn_gray = QPushButton("B/W")
        btn_color = QPushButton("Color")
        btn_contrast = QPushButton("Contrast")
        btn_blur = QPushButton("Blur")

        #Dropdown box
        filter_box = QComboBox()
        filter_box.addItem("Original")
        filter_box.addItem("Left")
        filter_box.addItem("Right")
        filter_box.addItem("Mirror")
        filter_box.addItem("Sharpness")
        filter_box.addItem("B/W")
        filter_box.addItem("Color")
        filter_box.addItem("Contrast")
        filter_box.addItem("Blur")

        picture_box = QLabel("Image will appear here")
        png_list = QListWidget()



        # Widgets:
        # - pushbutton
        # - list widget 
        # - combo box (drop down box)
        # - label
        # - widget



        # All Designs here
        master_layout = QHBoxLayout()

        col1 = QVBoxLayout()
        col2 = QVBoxLayout()

        col1.addWidget(btn_folder)
        col1.addWidget(list_file)
        col1.addWidget(filter_box)
        col1.addWidget(btn_left)
        col1.addWidget(btn_right)
        col1.addWidget(btn_mirror)
        col1.addWidget(btn_sharpness)
        col1.addWidget(btn_gray)
        col1.addWidget(btn_color)
        col1.addWidget(btn_contrast)
        col1.addWidget(btn_blur)

        col2.addWidget(picture_box)


        master_layout.addLayout(col1, 30)
        master_layout.addLayout(col2, 70)

        main_window.setLayout(master_layout)

    #Create all Functions here
    # def saveImage(self)


    
    
# Show/Run the App 

if __name__ == "__main__":
    app = QApplication([])
    main_window = Editor()
    main_window.show()
    app.exec_()




#QtCore -tools for aligning widgets
# #QtWidgets - tools for creating GUI elements


#PyQt Methods
#addWidget() - adds a widget to the layout
#setText() - sets the text of a widget
#addLayout() - adds a layout to a widget
#setLayout() - sets the layout of a widget
#show() - displays the widget on the screen


