from arduino_communication import arduinoCommunication
from handling_keys import handleKeys
import time
import cv2
import keyboard


if __name__ == "__main__" :
    keyObject = handleKeys() 
    arduino = arduinoCommunication(keyObject)
    #while True:                      
    arduino.transfer_data()
