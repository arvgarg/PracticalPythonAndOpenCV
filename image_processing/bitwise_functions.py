import cv2
import numpy as np

img_rect = np.zeros((500,500), dtype="uint8")
cv2.imshow("Rectangle", img_rect)
cv2.rectangle(img_rect, (250-100,250-100), (250+100,250+100), 255, -1)
cv2.imshow("Rectangle", img_rect)
cv2.waitKey(0)

img_circle = np.zeros((500,500), dtype="uint8")
cv2.circle(img_circle, (250,250), 125, 255, -1)
cv2.imshow("Circle", img_circle)
cv2.waitKey(0)

# Applying different types of bitwise operations
bitwise_AND = cv2.bitwise_and(img_rect, img_circle)
cv2.imshow("bitwise_AND", bitwise_AND)
cv2.waitKey(0)

bitwise_OR = cv2.bitwise_or(img_rect, img_circle)
cv2.imshow("bitwise_OR", bitwise_OR)
cv2.waitKey(0)

bitwise_XOR = cv2.bitwise_xor(img_rect, img_circle)
cv2.imshow("bitwise_XOR", bitwise_XOR)
cv2.waitKey(0)

bitwise_NOT = cv2.bitwise_not(img_rect)
cv2.imshow("bitwise_NOT", bitwise_NOT)
cv2.waitKey(0)

bitwise_NOT = cv2.bitwise_not(img_circle)
cv2.imshow("bitwise_NOT", bitwise_NOT)
cv2.waitKey(0)