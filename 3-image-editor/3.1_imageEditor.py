# Import Modules
import os
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton , QVBoxLayout, QHBoxLayout , QComboBox , QListWidget, QFileDialog # type: ignore
from PyQt5.QtCore import Qt # type: ignore
from PyQt5.QtGui import QPixmap
from PIL import Image, ImageFilter, ImageEnhance
from pathlib import Path

#App Settings
app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle("Image Editor")
main_window.setFixedSize(900, 700) # sets the size of the window to 400x200 pixels


# Main App Objects and settings
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

working_directory = ""
# folder = Path(r"C:\Users\Samsung\Projects\Python UI\pyqt-learning\3-image-editor")

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
        
        
        list_file.clear()
        for filename in filenames:
            list_file.addItem(filename)
        
        
    
    
def filter(self,files, extensions):
        results = []
        for file in files:
            for ext in extensions:
                if file.endswith(ext):
                    results.append(file)
        return results

# def apply_filter(self,filter_name):

filename = None

class Editor():

    def __init__(self):
        self.image = None
        self.original_img = None
        self.filename = None
        self.save_folder = "edits/"
                
    def load_image(self, filename):
        self.filename = filename
        fullname = os.path.join(working_directory, self.filename)
        self.image =Image.open(fullname)
        self.original_img = self.image.copy() #saves a copy in memory 
        
    def saveImage(self):
        path = os.path.join(working_directory, self.save_folder)
        if not(os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
            
        fullname = os.path.join(path, self.filename)
        self.image.save(fullname)

    def show_image(self, path):
        picture_box.hide()
        image = QPixmap(path)
        w, h = picture_box.width(), picture_box.height()
        image = image.scaled(w,h, Qt.KeepAspectRatio)
        picture_box.setPixmap(image)
        picture_box.show()
       
    def do_gray(self):
        self.image = self.image.convert("L")
        self.saveImage()
        image_path = os.path.join(working_directory,self.save_folder, self.filename)
        self.show_image(image_path)
        
    def do_left(self):
        self.image = self.image.transpose(Image.ROTATE_90)
        self.saveImage()
        image_path = os.path.join(working_directory,self.save_folder, self.filename)
        self.show_image(image_path)
        print("do left executed")
        
    def do_right(self):
        self.image = self.image.transpose(Image.ROTATE_270)
        self.saveImage()
        image_path = os.path.join(working_directory,self.save_folder, self.filename)
        self.show_image(image_path)
        
    def do_color(self):
        self.image = ImageEnhance.Color(self.image).enhance(1.2)
        self.saveImage()
        image_path=os.path.join(working_directory,self.save_folder,self.filename)
        self.show_image(image_path)
            
    def do_mirror(self):
        self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
        self.saveImage()
        image_path=os.path.join(working_directory,self.save_folder,self.filename)
        self.show_image(image_path)
                
    def do_contrast(self):
        self.image = contrast = ImageEnhance.Contrast(self.image)
        self.image = self.image.enhance(2.5)
        self.saveImage()
        image_path=os.path.join(working_directory,self.save_folder,self.filename)
        self.show_image(image_path)
        
    def do_blur(self):
        self.image =  self.image.filter(ImageFilter.BLUR)
        self.saveImage()
        image_path=os.path.join(working_directory,self.save_folder,self.filename)
        self.show_image(image_path) 
            
    def do_sharpen(self):
        self.image =  self.image.filter(ImageFilter.SHARPEN)
        self.saveImage()
        image_path=os.path.join(working_directory,self.save_folder,self.filename)
        self.show_image(image_path) 
                   
    def apply_filter(self, filter_name): #filter_box
        if filter_name == "Original":
            self.image = self.original_img.copy()
        else:
            filter_mapping = {
                "Left":lambda image: image.transpose(Image.ROTATE_90),
                "Right": lambda image: image.transpose(Image.ROTATE_270),
                "Mirror":lambda image: image.transpose(Image.FLIP_LEFT_RIGHT),
                "Sharpness": lambda image: image.filter(ImageFilter.SHARPEN),
                "B/W": lambda image: image.convert("L"),
                "Color": lambda image: ImageEnhance.Color(image).enhance(1.2),
                "Contrast": lambda image: ImageEnhance.Contrast(image).enhance(1.2),
                "Blur": lambda image: image.filter(ImageFilter.BLUR),
            }
            filter_function = filter_mapping.get(filter_name)
            if filter_function:
                self.image = filter_function(self.image)
                self.saveImage()
                image_path=os.path.join(working_directory,self.save_folder,self.filename)
                self.show_image(image_path) 
            pass
        self.saveImage()
        image_path=os.path.join(working_directory,self.save_folder,self.filename)
        self.show_image(image_path) 
    

            
            
def handle_filter():
    if list_file.currentRow() >=0:
        select_filter = filter_box.currentText()
        main.apply_filter(select_filter)

       
def displayImage():
    if list_file.currentRow() >= 0:
        filename = list_file.currentItem().text()
        main.load_image(filename)
        main.show_image(os.path.join(working_directory, main.filename))
    
    # filter files and extensions


    


main = Editor()

btn_folder.clicked.connect(getWorkDirectory)
list_file.currentRowChanged.connect(displayImage)
filter_box.currentTextChanged.connect(handle_filter)    

btn_left.clicked.connect(main.do_left)
btn_right.clicked.connect(main.do_right)
btn_mirror.clicked.connect(main.do_mirror)
btn_sharpness.clicked.connect(main.do_sharpen)
btn_gray.clicked.connect(main.do_gray)
btn_color.clicked.connect(main.do_color)
btn_contrast.clicked.connect(main.do_contrast)
btn_blur.clicked.connect(main.do_blur)


main_window.show()
app.exec_()

# Show/Run the App 

# if __name__ == "__main__":
    
#     # main_window = Editor()
#     main_window.show()
#     app.exec_()


