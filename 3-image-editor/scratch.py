
black_white = picture.convert("L")
black_white.save(image_path / "gray.png")

mirror = picture.transpose(Image.FLIP_LEFT_RIGHT)
mirror.save(image_path / "mirrored.png")

blur = picture.filter(ImageFilter.BLUR)
blur.save(image_path / "blurred.png")


#ImageEnhance
contrast = ImageEnhance.Contrast(picture)
contrast = contrast.enhance(2.5)
contrast.save(image_path / "contrast.png")

color = ImageEnhance.Color(picture).enhance(2.5)
color.save(image_path / "color.png")
# Make sure extension you save with 



    
def do_black_white(self):
    
    
black_white = picture.convert("L")
black_white.save(image_path / "gray.png")