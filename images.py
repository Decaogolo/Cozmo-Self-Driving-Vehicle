import PIL
from PIL import Image, ImageFilter, ImageEnhance, ImageOps

image = Image.open("0.jpg")

print(image)

image = image.crop((140,100,180,140))

#image = image.filter(ImageFilter.FIND_EDGES)
#image = image.convert(mode="L")
enhancer = ImageEnhance.Contrast(image)

image = enhancer.enhance(5.0)
image = ImageOps.invert(image)
image = image.convert(mode="1")

print(list(image.getdata()))
print("width",image.width,"\nheight",image.height)
print(image.getpixel((20,20)))
image.save("00.jpg")
