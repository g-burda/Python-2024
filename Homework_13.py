from PIL import Image, ImageOps

image1 = Image.open('pet_rat.jpg')
print(image1.mode) 
print(image1.size)  
print(image1.width)   
print(image1.height)   
print(image1.format)   
image1.show()

with Image.open("pet_rat.jpg") as image2:
    thumbnail_size = (128, 128)
    thumbnail_image = ImageOps.fit(image2, thumbnail_size)
    thumbnail_image.save("pet_rat_thumbnail.jpg", "JPEG")