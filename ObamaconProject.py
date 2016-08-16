from PIL import Image
im = Image.open("three.jpg")
crimson = (220, 20, 60)
darkOrange = (255, 140, 0)
yellow = (255, 255, 0)
emeraldGreen = (0, 201, 87)
slateBlue3 = (105, 89, 205)
purple = (128, 0, 128)


data = im.getdata()
dataList = list(data)
newList = []


for i in dataList:
	pixel = i[0] + i[1] + i[2]
	if pixel > 629:
		colorOne = crimson
		newList.append(colorOne)
	elif pixel >503 and pixel <= 629: 
		colorTwo = darkOrange
		newList.append(colorTwo)
	elif pixel >377 and pixel <= 503:
		colorThree = yellow
		newList.append(colorThree)
	elif pixel >251 and pixel <=377:
		colorFour = emeraldGreen
		newList.append(colorFour)
	elif pixel >125 and pixel <=251:
		colorFive = slateBlue3
		newList.append(colorFive)	
	else:
		colorSix = purple
		newList.append(colorSix)
im.putdata(newList)
newIm = Image.new("RGB", (600, 400))
im.save("threetwo.jpg")
