import mediapipe as mp
import cv2
import numpy as np
import time

#contants
ml = 150
max_x, max_y = 250+ml, 50
curr_tool = "select tool"
time_init = True
rad = 40
var_inits = False
thick = 4
prevx, prevy = 0,0

#get tools function
def getTool(x):
	if x < 50 + ml:
		return "line"

	elif x<100 + ml:
		return "rectangle"

	elif x < 150 + ml:
		return"draw"

	elif x<200 + ml:
		return "circle"

	else:
		return "erase"

def index_raised(yi, y9):
	if (y9 - yi) > 40:
		return True

	return False



hands = mp.solutions.hands
hand_landmark = hands.Hands(min_detection_confidence=0.6, min_tracking_confidence=0.6, max_num_hands=1)
draw = mp.solutions.drawing_utils


# drawing tools
tools = cv2.imread("tools.png")
#tools = tools.astype('uint8')

mask = np.ones((480, 640))*255
mask = mask.astype('uint8')
'''
tools = np.zeros((max_y+5, max_x+5, 3), dtype="uint8")
cv2.rectangle(tools, (0,0), (max_x, max_y), (0,0,255), 2)
cv2.line(tools, (50,0), (50,50), (0,0,255), 2)
cv2.line(tools, (100,0), (100,50), (0,0,255), 2)
cv2.line(tools, (150,0), (150,50), (0,0,255), 2)
cv2.line(tools, (200,0), (200,50), (0,0,255), 2)
'''

cap = cv2.VideoCapture(0)
while True:
	_, frm = cap.read()
	frm = cv2.flip(frm, 1)



	cv2.imshow("Video", frm)
