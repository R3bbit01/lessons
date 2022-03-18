from PIL import Image

img = Image.open("beach.jpg")
img2 = Image.open("cactus.jpg")

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
        r2, g2, b2 = pixels_overlay[x, y]
        if r2 != that_value_on_pixel_0_0:
            r = r2
        r_new = r
        pixels_new[x, y] = (r_new, g, b)
image_new.show()