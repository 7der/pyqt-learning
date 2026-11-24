# Import Modules
import os
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton , QVBoxLayout, QHBoxLayout , QComboBox , QListWidget, QFileDialog # type: ignore
from PyQt5.QtCore import Qt # type: ignore
from PyQt5.QtGui import QPixmap
from PIL import Image, ImageFilter, ImageEnhance
from pathlib import Path



# folder = Path(r"C:\Users\Samsung\Projects\Python UI\pyqt-learning\3-image-editor")

class Editor(QWidget):

    def __init__(self):
        
        super().__init__()
        
        # Main App Objects and settings
       
        #main_window = QWidget()
        self.setWindowTitle("Image Editor")
        self.setFixedSize(900, 700) # sets the size of the window to 400x200 pixels

        # 
        self.working_directory = ""
        self.image = None
        self.original_img = None
        self.filename = None
        self.save_folder = "edits/"
                
        blank_list = []


        # Create all Objects/widgets
        self.btn_folder = QPushButton("Select Folder")
        self.list_file= QListWidget()

        # buttons = ["Left", "Right", "Mirror", "Sharpness", "B/W", "Color", "Contrast"]
                
        self.btn_left= QPushButton("Left")
        self.btn_right = QPushButton("Right")
        self.btn_mirror = QPushButton("Mirror")
        self.btn_sharpness = QPushButton("Sharpness")
        self.btn_gray = QPushButton("B/W")
        self.btn_color = QPushButton("Color")
        self.btn_contrast = QPushButton("Contrast")
        self.btn_blur = QPushButton("Blur")

        #Dropdown box
        self.filter_box = QComboBox()
        self.filter_box.addItem("Original")
        self.filter_box.addItem("Left")
        self.filter_box.addItem("Right")
        self.filter_box.addItem("Mirror")
        self.filter_box.addItem("Sharpness")
        self.filter_box.addItem("B/W")
        self.filter_box.addItem("Color")
        self.filter_box.addItem("Contrast")
        self.filter_box.addItem("Blur")

        self.picture_box = QLabel("Image will appear here")
        png_list = QListWidget()



        # All Designs here
        master_layout = QHBoxLayout()

        col1 = QVBoxLayout()
        col2 = QVBoxLayout()

        col1.addWidget(self.btn_folder)
        col1.addWidget(self.list_file)
        col1.addWidget(self.filter_box)
        col1.addWidget(self.btn_left)
        col1.addWidget(self.btn_right)
        col1.addWidget(self.btn_mirror)
        col1.addWidget(self.btn_sharpness)
        col1.addWidget(self.btn_gray)
        col1.addWidget(self.btn_color)
        col1.addWidget(self.btn_contrast)
        col1.addWidget(self.btn_blur)

        col2.addWidget(self.picture_box)


        master_layout.addLayout(col1, 30)
        master_layout.addLayout(col2, 70)

        self.setLayout(master_layout)
        self.btn_folder.clicked.connect(self.getWorkDirectory)
        self.list_file.currentRowChanged.connect(self.displayImage)
        
    # #Create all Functions here
    
    def load_image(self, filename):
        self.filename = filename
        fullname = os.path.join(working_directory, self.filename)
        self.image =Image.open(fullname)
        self.original_img = self.image.copy() #saves a copy in memory 
        
    def saveImage(self):
        path = os.path.joi(working_directory, self.save_folder)
        if not(os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
            
        fullname = os.path.join(path, self.filename)
        self.image.save(fullname)

    def show_image(self, path):
        self.picture_box.hide()
        image = QPixmap(path)
        w, h = self.picture_box.width(), self.picture_box.height()
        image = image.scaled(w,h, Qt.KeepAspectRatio)
        self.picture_box.setPixmap(image)
        self.picture_box.show()
       
    def displayImage(self):
        if self.list_file.currentRow() >= 0:
            self.filename = self.list_file.currentItem().text()
            main_window.load_image(self.filename)
            main_window.show_image(os.path.join(working_directory, main_window.filename))
    
    # filter files and extensions
    def filter(self,files, extensions):
        results = []
        for file in files:
            for ext in extensions:
                if file.endswith(ext):
                    results.append(file)
        return results
    
    def getWorkDirectory(self):
        global working_directory 
        filenames =[]
        working_directory = QFileDialog.getExistingDirectory()
        # extensions = [ '.jpg', '.jpeg', '.png', '.svg']
        extensions = (".jpg", ".png", ".jpeg", ".svg")
        
        # filenames = [ filter(os.listdir(working_directory), extensions)
        filenames = [ 
            f for f in os.listdir(working_directory) 
            if f.lower().endswith(extensions) 
            ]
        
        
        self.list_file.clear()
        for filename in filenames:
            self.list_file.addItem(filename)
        
        
    # def btn_folder_clicked(self):
    #     self.getWorkDirectory()
    
    # def do_color(self):
        #     self.image = ImageEnhance.Color(self.image).enhance(1.2)
        #     self.saveImage()
        #     image_path=os.path.join(work_directory,self.save_folder,self.file)
        #     self.showImage(image_path)
    
        # def do_black_white(self):
        #     self.image = self.image.convert("L")
        #     self.saveImage()
        #     image_path=os.path.join(work_directory,self.save_folder,self.file)
        #     self.showImage(image_path)
        
        # def do_mirror(self):
        #     self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
        #     self.saveImage()
        #     image_path=os.path.join(work_directory,self.save_folder,self.file)
        #     self.showImage(image_path)
            
        # def do_contrast(self):
        #     self.image = contrast = ImageEnhance.Contrast(self.image)
        #     self.image = self.image.enhance(2.5)
        #     self.saveImage()
        #     image_path=os.path.join(work_directory,self.save_folder,self.file)
        #     self.showImage(image_path)
    
        # def do_blur(self):
        #     self.image =  self.image.filter(ImageEnhance.BLUR)
        #     self.saveImage()
        #     image_path=os.path.join(work_directory,self.save_folder,self.file)
        #     self.showImage(image_path) 2
            
    
        
        # file_list.currentRowChanged.connect(displayImage)
        # btn_color.clicked.connect(main.do_color)
    
    
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


