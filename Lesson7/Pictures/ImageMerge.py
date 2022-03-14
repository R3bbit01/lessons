#This line imports or includes the library we will need
from PIL import Image

#Open Image
#Img = Image.open("cactus.jpg")

#Make a copy the image so that the
#original image does not get affected
#Img = Img.copy()
img = Image.open("beach.jpg")
img2 = Image.open("cactus.jpg")
#Img = Img.copy()

#Paste image giving dimensions
#Img.paste(Image.copy, (70, 150))

#Save the image
#Img.save('NewImage.jpg')


#width, height = img.size
#pixels_original = image.original.load()

#pixels_new[x, y] = (r, g, b)
image_new = Image.new("RGB", img.size)
pixels_new = image_new.load()
pixels_original = img.load()
pixels_overlay = img2.load()
size = img.size
print(img.size)
width = size[0]
height = size[1]
that_value_on_pixel_0_0 = img2[0,0]
for x in range(width):
    for y in range(height):
        r, g, b = pixels_original[x, y]
        r2, g2, b2 = pixels_overlay[x,y]
        if r2 != that_value_on_pixel_0_0:
            r = r2
        r_new = r
        pixels_new[x, y] = (r_new, g, b)
image_new.show()
# print(r, g, b)
# print(img.size)