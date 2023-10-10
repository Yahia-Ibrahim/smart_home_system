import serial
import cv2
from fingers_counter import handDetection
from handling_keys import handleKeys
import time

"""
the class here receives the data from the core program and communicate with arduino through serial connection
"""
class arduinoCommunication:
    def __init__(self, key) :
        self.hands = handDetection()  
        self.key = key  
        #self.arduino = serial.Serial('COM5', 9600)
        #time.sleep(1) #give the connection a second to settle
    def transfer_data(self):
        while not self.key.esc:
            success, img = self.hands.cap.read()
            img = cv2.flip(img, 1)

            #reading data from hand_gester_detection function is surrounded by try and catch block because it would crash if no hands were detected
            try:
                fingerCount, dist = self.hands.hand_gester_detection(img)

                if self.key.task1_status:
                    #string = "L" + " " + str(fingerCount)
                    #self.arduino.write(string.encode())
                    #time.sleep(0.05)
                    cv2.putText(img, str(fingerCount), (150, 150), cv2.FONT_HERSHEY_PLAIN, 12, (255, 0, 0), 12)
                    
                elif self.key.task2_status:
                    range = 0
                    if dist > 0 and dist <= 150:
                        range = 0
                    elif dist > 150 and dist <= 300:
                        range = 3
                    elif dist > 300 and dist <= 450:
                        range = 6
                    else:
                        range = 9
                    #string = "S" + " " + str(range)
                    #self.arduino.write(string.encode())
                    #time.sleep(0.05)
                    cv2.putText(img, str(dist), (50, 200), cv2.FONT_HERSHEY_PLAIN, 5, (255, 0, 0), 12)
                #elif self.key.temperature_read:
                #    self.arduino.write("T".encode())
                #    time.sleep(0.05)
                #    self.receive_data()
                #elif self.key.LDR_read:
                #   self.arduino.write("B".encode())
                #    time.sleep(0.05)
                #    self.receive_data()
            except:
                pass                        
            cv2.imshow("Finger Counter", img)
            key = cv2.waitKey(10) & 0xFF
            self.key.keyInput(key)
        else:
            #self.arduino.close()
            self.hands.cap.release()
            cv2.destroyAllWindows() 

       
    #def receive_data(self):
        
    #    data = self.arduino.readline().decode('ascii')
    #    if data:
    #        if self.key.temperature_read:
    #            print(f"temperature sensor reading : {data}")
    #        else:
    #            print(f"LDR sensor reading : {data}")

