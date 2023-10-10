import cv2
import mediapipe as mp
import math

"""
this is the core program that performs the finger counting operation and other calculations behind the scenes
"""
class handDetection :
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands()
        self.mpDraw = mp.solutions.drawing_utils
        self.fingerCoordinates = [(8, 6), (12, 10), (16, 14), (20, 18)]
        self.thumbCoordinate = (4, 2)
    def hand_gester_detection(self, img):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = self.hands.process(imgRGB)
        multiLandMarks = results.multi_hand_landmarks

        if multiLandMarks:
            handPoints = []

            for handLms in multiLandMarks:
                self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)

                for idx, lm in enumerate(handLms.landmark):   
                    h, w, c = img.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    handPoints.append((cx, cy))

            for point in handPoints:
                cv2.circle(img, point, 10, (0, 0, 255), cv2.FILLED)
            
            upCount = 0

            for coordinate in self.fingerCoordinates:
                if handPoints[coordinate[0]][1] < handPoints[coordinate[1]][1]:
                    upCount += 1

            if handPoints[self.thumbCoordinate[0]][0] < handPoints[self.thumbCoordinate[1]][0]:   #would work only with the right hand
                upCount += 1

            x_dist = handPoints[4][0] - handPoints[8][0]
            y_dist = handPoints[4][1] - handPoints[8][1]
            dist = int(math.sqrt(x_dist**2 + y_dist**2))
            
            return upCount, dist


