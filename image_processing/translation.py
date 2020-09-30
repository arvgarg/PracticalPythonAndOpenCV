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

# matrix M is the translation matrix
M = np.array([[1,0,50],
                [0,1,100]], dtype = np.float32)

h,w = image.shape[:2]

translated_img = cv2.warpAffine(image, M, (h,w))
cv2.imshow("Translated image", translated_img)
cv2.waitKey(0)

from imutils import translate
translated_img = translate(image, 100, -100)
cv2.imshow("Translated image", translated_img)
cv2.waitKey(0)