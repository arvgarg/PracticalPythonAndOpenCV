import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True,
                help="Path to input image")
args = vars(ap.parse_args())

image = cv2.imread(args["input"])
cv2.imshow("Image", image)
cv2.waitKey(0)

# resize according to either width or height
old_h, old_w = image.shape[:2]

# resizing with new width given and maintaining the aspect ratio
new_w = 300
ratio = new_w/float(old_w)
new_h = int(old_h * ratio)
resized_img = cv2.resize(image, (new_w,new_h), interpolation = cv2.INTER_AREA)

cv2.imshow("Resized Image", resized_img)
cv2.waitKey(0)

# resizing with new height given and maintaining the aspect ratio
new_h = 700
ratio = new_h/float(old_h)
new_w = int(old_w * ratio)

resized_img = cv2.resize(image, (new_w,new_h))
cv2.imshow("Resized Image", resized_img)
cv2.waitKey(0)

from imutils import resize
resized_img = resize(image, width=300)
cv2.imshow("Resized Image", resized_img)
cv2.waitKey(0)

resized_img = resize(image, height=800)
cv2.imshow("Resized Image", resized_img)
cv2.waitKey(0)