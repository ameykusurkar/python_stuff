import Image

img = Image.open('red.png')

width, height = 96, 128

count = 0
for x in range(0, width, width/3):
  for y in range(0, height, height/4):
    count += 1
    print x, y
    newimg = img.crop((x, y, x + width/3, y + height/4))
    newimg.save('redsprites/redpart{}.png'.format(count))

