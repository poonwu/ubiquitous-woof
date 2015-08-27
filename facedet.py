import cv2
import math

MAIN_WINDOW = "Onward"
TILT_ANGLE = 30
CLASSIFIER_FILE = "haarcascade_frontaltface.xml"

# Read image
img = cv2.imread('gates.jpg')
edges = cv2.Canny(img,100,200)
face_cascade = cv2.CascadeClassifier(CLASSIFIER_FILE)

faces = face_cascade.detectMultiScale(img, 1.3, 5)
for (x,y,w,h) in faces:
	cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

# create window
cv2.namedWindow(MAIN_WINDOW)
cv2.imshow(MAIN_WINDOW, img)


while(True):
	pressed_key = cv2.waitKey(5)
	if pressed_key != -1 and pressed_key not in [65365, 65366]:
		break