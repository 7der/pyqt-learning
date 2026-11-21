from PIL import Image, ImageFilter, ImageEnhance
from pathlib import Path

# folder = Path("3-image-editor")
# print(folder)

image_path = Path(r"C:\Users\Samsung\Projects\Python UI\pyqt-learning\3-image-editor")


# print("Looking for this: ", (folder / "123.jpg").resolve())
with Image.open(image_path / "123.jpg" ) as picture:
    # picture.show()
    
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
    # Make sure extension you save with is the same with the original
    
    
    