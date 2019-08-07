import cv2
import numpy as np
from matplotlib import pyplot as plt
np.set_printoptions(threshold=np.nan)

img = cv2.imread("turbine-blade.jpg",0)
mask = [[-1,-1,-1],[-1,8,-1],[-1,-1,-1]]
#mask = [[1,1,1],[1,-8,1],[1,1,1]]

mask = np.asarray(mask)
height,width = img.shape
#print(img.shape)
image = [[ 0 for x in range(width)] for w in range(height)]
image = np.asarray(image)
imgp = [[ 0 for x in range(width + 2)] for w in range(height + 2)]
imgp = np.asarray(imgp)
imgm = [[ 0 for x in range(width + 2)] for w in range(height + 2)]
imgm = np.asarray(imgm)

for i in range(height):
	for j in range(width):
		imgp[i+1][j+1] = img[i][j]

for i in range(height):
	for j in range(width):
		imgm[i+1][j+1] = imgp[i][j]*mask[0][0] + imgp[i][j+1]*mask[0][1] + imgp[i][j+2]*mask[0][2] + imgp[i+1][j]*mask[1][0] + imgp[i+1][j+1]*mask[1][1] + imgp[i+1][j+2]*mask[1][2] + imgp[i+2][j]*mask[2][0] + imgp[i+2][j+1]*mask[2][1] + imgp[i+2][j+2]*mask[2][2]
for i in range(height):
	for j in range(width):
		image[i][j]= imgm[i+1][j+1]
#image = image/255
#cv2.imshow("Image",image)
#cv2.waitKey(0)

for i in range(height):
	for j in range(width):
		if(image[i][j]<0):
			image[i][j] *= -1
c = 0
for i in range(height):
	for j in range(width):
		if(image[i][j]>c):
			c = image[i][j] 
print(c)
maxLoc = []
for i in range(height):
	for j in range(width):
		if(image[i][j]>=1000):
			image[i][j] =255
			print("Pixel Position is::", i ,j )
			print("Considering top left corner of the image as origin (0,0) the coordinates of the detected point are:", j , -i)
			x = i 
			y = j
		else:
			image[i][j] =0


#image = image/255
#cv2.imshow("Image",image)
#cv2.waitKey(0)
img1 = cv2.imread("turbine-blade.jpg",1)
img1 = cv2.rectangle(img1, (y-5, x-5), (y+5, x+5), (0, 0, 255), 2)
cv2.imwrite("point-detected.jpg",image)
cv2.imwrite("point-loc.jpg",img1)
	