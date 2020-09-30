import argparse
import numpy as np
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True,
                help="Path to input image")
args = vars(ap.parse_args())

image = cv2.imread(args["input"])
cv2.imshow("Original Image", image)
cv2.waitKey(0)

(B, G, R) = cv2.split(image)

print(type(B))
print(B.shape) # only 2 dimensions, width and height
cv2.imshow("Blue channel in grayscale", B) #Blue channel but in grayscale
cv2.waitKey(0)

# To see actual blue channel, our image needs to have 3 dimensions
# that is we need to add red and green channel arrays and fill them with 0s
# If we provide an image with only width and height to cv2.imshow(), it treats it
# as a greyscale image and hence displays as such
zero_arr = np.zeros(image.shape[:2], dtype="uint8")

# To show each individual channel in their respective colors, we need to
# convert the image to RGB(so that it has 3 dimensions) by adding 2 more 
# additional channels and fill those 2 channels with 0s
# Now we use the merge function, and place each of the channels in their
# correct order of BGR
blue_channel = cv2.merge([B, zero_arr, zero_arr])
cv2.imshow("Blue channel", blue_channel)
cv2.waitKey(0)

green_channel = cv2.merge([zero_arr, G, zero_arr])
cv2.imshow("Green channel", green_channel)
cv2.waitKey(0)

red_channel = cv2.merge([zero_arr, zero_arr, R])
cv2.imshow("Red channel", red_channel)
cv2.waitKey(0)