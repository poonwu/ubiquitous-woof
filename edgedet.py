import cv2
import math

MAIN_WINDOW = "Onward"
TILT_ANGLE = 30
CLASSIFIER_FILE = "haarcascade_frontaltface.xml"

def rotate_image(image, angle):
    h, w = image.shape[:2]
    matrix = cv2.getRotationMatrix2D((w * 0.5, h * 0.5), angle, 0.9)
    return cv2.warpAffine(image, matrix, (w, h), flags=cv2.INTER_LINEAR)

def detect_face(classifier, img, angle):
	faces = classifier.detectMultiScale(
		rotate_image(img, angle),
		scaleFactor=1.3,
		minNeighbors=3,
		minSize=(120, 120)
	)
	#,
	#	flags=cv2.cv.CV_HAAR_FIND_BIGGEST_OBJECT | cv2.cv.CV_HAAR_DO_ROUGH_SEARCH
	return rotate_point(faces[-1], img, -angle) if len(faces) else None

# Read image
img = cv2.imread('messi5.jpg',0)
edges = cv2.Canny(img,100,200)
classifier = cv2.CascadeClassifier(CLASSIFIER_FILE)

# create window
cv2.namedWindow(MAIN_WINDOW)
cv2.imshow(MAIN_WINDOW, img)


for angle in [-TILT_ANGLE, TILT_ANGLE]:
	face = detect_face(classifier, img, angle)
	if not face:
		print "No face!"
		continue

	#draw box around face
	x, y, w, h = face
	cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

while(True):
	pressed_key = cv2.waitKey(5)
	if pressed_key != -1 and pressed_key not in [65365, 65366]:
		break