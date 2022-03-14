#This line imports or includes the library we will need
from PIL import Image

#Open Image
Img1 = Image.open("cactus.jpg")

#Make a copy the image so that the
#original image does not get affected
Img = Img1.copy()
Img = Img.open("beach.jpg")
Img = Img.copy()

#Paste image giving dimensions
Img.paste(Image.copy, (70, 150))

#Save the image
Img.save('NewImage.jpg')