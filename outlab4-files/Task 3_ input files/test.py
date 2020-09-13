from PIL import Image
img = Image.open('Lenna.png')

unique_colors = set()
for i in range(img.size[0]):
    for j in range(img.size[1]):
        pixel = img.getpixel((i, j))
        unique_colors.add(pixel)

print('Image info = ', img)
print('Unique color count = ', len(unique_colors))