import cv2
import math

MAIN_WINDOW = "Onward"

probe_file = 'messi5_defect.jpg'     # probe input
base_file = 'messi5.jpg'             # base file is first acceptable input 

# Thoughts: 
# we take N samples of non-defects and M samples of defects
# For N+M output we can use linear classifier to classify unseen samples into group of non-defects or defects
#

# Read image
defect_img = cv2.imread(probe_file, 0)
defect_edge = cv2.Canny(defect_img,100,200)

img1 = cv2.imread(base_file, 0)
edges1 = cv2.Canny(img1,100,200)

exor = defect_edge ^ edges1 

# create window
cv2.namedWindow(MAIN_WINDOW)
cv2.imshow(MAIN_WINDOW, exor)

while(True):

	pressed_key = cv2.waitKey(5)
	if pressed_key != -1 and pressed_key not in [65365, 65366]:
		break