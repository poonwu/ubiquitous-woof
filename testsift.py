import cv2
import math
import numpy as np

MAIN_WINDOW = 'SIFT'
A = cv2.imread('images/starbucks_small.jpg', 0)
B = cv2.imread('images/starbucks_small_defect3.jpg', 0)

#sift object
sift = cv2.xfeatures2d.SIFT_create()

kp1, des1 = sift.detectAndCompute(A,None)
kp2, des2 = sift.detectAndCompute(B,None)

#brute force matcher
bf = cv2.BFMatcher()
# Match descriptors.
matches = bf.knnMatch(des1,des2, k=2)

# Apply ratio test
good = []
for m,n in matches:
	# analyze each pair
    if m.distance < 0.2*n.distance:
    	# lower is better, DMatches distances are
    	# score of similarity between the two
    	# descriptors of a match. 
        good.append([m])

for i in range(len(good)):
	pt1 = kp1[good[i][0].queryIdx].pt
	pt2 = kp2[good[i][0].trainIdx].pt

	print pt1[0] - pt2[0]

img3 = None
img3 = cv2.drawMatchesKnn(A,kp1,B,kp2,good,img3, flags=2)

cv2.namedWindow(MAIN_WINDOW)
cv2.imshow(MAIN_WINDOW, img3)

while(True):

	pressed_key = cv2.waitKey(5)
	if pressed_key != -1 and pressed_key not in [65365, 65366]:
		break