import cv2
import math

MAIN_WINDOW = "Onward"
TILT_ANGLE = 30

# Read image
img0 = cv2.imread('gates_defect.jpg', 0)
edges0 = cv2.Canny(img0,300,430)

img1 = cv2.imread('gates.jpg', 0)
edges1 = cv2.Canny(img1,300,430)

exor = edges0 ^ edges1

# create window
cv2.namedWindow(MAIN_WINDOW)
cv2.imshow(MAIN_WINDOW, exor)

while(True):
	pressed_key = cv2.waitKey(5)
	if pressed_key != -1 and pressed_key not in [65365, 65366]:
		break