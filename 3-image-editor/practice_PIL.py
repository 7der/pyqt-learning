from PIL import Image, ImageFilter, ImageEnhance
from pathlib import Path 

folder = Path("3 Image Editor")

with Image.open(folder / "123.JPG") as picture:
    # picture.show()
    
    black_white = picture.convert("L")
    black_white.save(folder / "gray.png")
    
    mirror = picture.transpose(Image.FLIP_LEFT_RIGHT)
    mirror.save(folder / "mirrored.png")
    
    blur = picture.filter(ImageFilter.BLUR)
    blur.save(folder / "blurred.png")
    
    
    #ImageEnhance
    contrast = ImageEnhance.Contrast(picture)
    contrast = contrast.enhance(2.5)
    contrast.save(folder / "contrast.png")
    
    color = ImageEnhance.Color(picture).enhance(2.5)
    color.save(folder / "color.png")
    # Make sure extension you save with is the same with the original
    
    
    