import cv2
import math
import numpy as np

base_file = 'images/starbucks_small.jpg'             # base file is first acceptable input 

# Thoughts: 
# we take N samples of non-defects and M samples of defects
# For N+M output we can use linear classifier to classify unseen samples into group of non-defects or defects
#

def rotate_image(image, angle):
    h, w = image.shape[:2]
    matrix = cv2.getRotationMatrix2D((w , h ), angle, 1)
    return cv2.warpAffine(image, matrix, (w, h), flags=cv2.INTER_LINEAR)

def auto_transform(image):
	#TODO: will need to be able to 
	#automatically fix image scale and rotation
	pass

def get_edges(img):
	th = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)
	ed = cv2.Canny(th,222,333)

	return (th, ed)

def compare_gti(probe_img_name, ground_truth_img):
	# Initiate SIFT detector
	#sift = cv2.SIFT()
	# read original image and extract features
	probe_img = cv2.imread(probe_img_name, 0)
	#kp1, des1 = sift.detectAndCompute(probe_img,None)

	# Edge Detect
	(probe_thres, probe_edge) = get_edges(probe_img)
	# Rotate to fit
	subject =  rotate_image(probe_edge, 0)

	# get differences
	finalx =  ground_truth_img ^ subject
	# create window
	cv2.namedWindow(probe_img_name )
	cv2.imshow(probe_img_name, finalx)

	# create debugger
	#blended = cv2.addWeighted( defect_img, 0.1, img1, 0.5, 0.0);

	#cv2.namedWindow(probe_img_name + " Original")
	#cv2.imshow(probe_img_name + " Original", defect_img)


img1 = cv2.imread(base_file, 0)
(img1_th, edges1) = get_edges(img1)

compare_gti('images/starbucks_small_defect.jpg', edges1)
compare_gti('images/starbucks_small_defect2.jpg', edges1)
compare_gti('images/starbucks_small_defect4.jpg', edges1)
compare_gti('images/starbucks_small_defect4.jpg', edges1) # defect3 does not align perfectly

while(True):

	pressed_key = cv2.waitKey(5)
	if pressed_key != -1 and pressed_key not in [65365, 65366]:
		breaks