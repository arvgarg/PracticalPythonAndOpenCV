import argparse
import cv2

ap = argparse.ArgumentParser()

ap.add_argument("-i", "--input", required=True,
                help="Path to input image")

args = vars(ap.parse_args())
print(args)

image = cv2.imread(args["input"])
print(image.shape)
print("Height of img is {} pixels".format(image.shape[0]))
print("Width of img is {} pixels".format(image.shape[1]))
print("Channels in img {}".format(image.shape[2]))

corner = image[:100,:100]
print(corner[:,:,0])
cv2.imshow("Corner", corner)

image[0:100, 0:100] = (0, 255, 0)

cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.imwrite("newimage.jpg", image)
