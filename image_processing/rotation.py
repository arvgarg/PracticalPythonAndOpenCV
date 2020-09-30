import argparse
import cv2
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True,
                help="Path to input image")
args = vars(ap.parse_args())

image = cv2.imread(args["input"])
cv2.imshow("Image",image)
cv2.waitKey(0)

h,w = image.shape[:2]
centerX, centerY = w//2, h//2

# matrix M is the translation matrix
M = cv2.getRotationMatrix2D((centerX, centerY), 45, 1.0)

rotated_img = cv2.warpAffine(image, M, (w,h))
cv2.imshow("Rotated Image", rotated_img)
cv2.waitKey(0)

from imutils import rotate
rotated_img = rotate(image, -45)
cv2.imshow("Rotated Image", rotated_img)
cv2.waitKey(0)