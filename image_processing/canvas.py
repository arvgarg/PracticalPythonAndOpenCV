import numpy as np
import cv2

# Creating an empty canvas
canvas = np.zeros((300,300,3), dtype = "uint8")

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# Drawing lines
green = (0,255,0)
cv2.line(canvas, (0,0), (300,300), green)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

red = (0,0,255)
cv2.line(canvas, (0,0), (300,300), red, 7)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

blue = (255,0,0)
cv2.line(canvas, (0,0), (300,300), blue, 3)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# Drawing rectangles
cv2.rectangle(canvas, (50,50), (150,200), green, 3)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

cv2.rectangle(canvas, (70,220), (250,280), blue, -1)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# Drawing circles
cv2.circle(canvas, (250,50), 30, red, 10)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

CentreX, CentreY = canvas.shape[1]//2, canvas.shape[0]//2
white = (255,255,255)
cv2.circle(canvas, (CentreX,CentreY), 50, white, -1)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# Creating an empty canvas
canvas = np.zeros((300,300,3), dtype = "uint8")

for i in range(0,25):
    center = tuple(np.random.randint(low=0,high=301, size=(2,)))
    radius = np.random.randint(low=0,high=200)
    color = np.random.randint(low=0,high=256, size=(3,)).tolist()
    
    if i%2==0:
        cv2.circle(canvas, center, radius, color, -1)
    else:
        cv2.circle(canvas, center, radius, color, 7)
    cv2.imshow("Image", canvas)
cv2.waitKey(0)