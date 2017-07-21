#Obamicon
#Obama Come Back

darkBlue = (47,79,79)
red = (233,150,122)
lightBlue = (175, 238,238)
yellow = (255, 192, 203)

from PIL import Image

im = Image.open("pop.jpg")

pixeldata = list(im.getdata())
listofpixels=len(pixeldata)

for i in range(listofpixels):
    redpixelvalue = pixeldata[i][0]
    greenpixelvalue = pixeldata[i][1]
    bluepixelvalue = pixeldata[i][2]
    sum = redpixelvalue + greenpixelvalue + bluepixelvalue
    #print(sum)

    if sum < 182:
        pixeldata[i] = darkBlue
    elif sum >= 182 and sum < 364:
        pixeldata[i] = red
    elif sum >= 364 and sum < 546:
        pixeldata[i] = lightBlue
    else:
        pixeldata[i]= yellow
new_image = Image.new (im.mode, im.size)
new_image.putdata(pixeldata)
new_image.show()
