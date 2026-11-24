cube = lambda x:x**3
result =cube(4)
print(result)

multi_numbers = lambda x,y:x*y
result = multi_numbers(2,3)
print(result)

filter_box_dict = {1:'Original',2:'',3:'',4:'',5:'',6:'',7:''}

filter_mapping = {
    "Left":lambda self.image.image.transpose(Image.ROTATE_90)
    "Right": lambda self.image.transpose(Image.ROTATE_270)
    "Mirror":lambda self.image.transpose(Image.FLIP_LEFT_RIGHT)
    "Sharpness": lambda
    "B/W": lambda self.image.convert("L")
    "Color": lambda ImageEnhance.Color(self.image).enhance(1.2)
    "Contrast": lambda contrast = ImageEnhance.Contrast(self.image)
    "Blur": lambda self.image.filter(ImageFilter.BLUR)
}



  