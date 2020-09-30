import argparse
import cv2
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True,
                help="Path to input image")
args = vars(ap.parse_args())

image = cv2.imread(args["input"])
cv2.imshow("Original Image", image)
cv2.waitKey(0)

mask = np.zeros(image.shape[:2], dtype="uint8")
h,w = image.shape[:2]
cv2.rectangle(mask, (500,100), (900,500), 255, -1)
cv2.imshow("Mask", mask)
cv2.waitKey(0)

result = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Result", result)
cv2.waitKey(0)