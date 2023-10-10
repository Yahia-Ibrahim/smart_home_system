import cv2
import keyboard

"""
the class here ensures there is only one task running at a time to avoid sending conflicting data to arduino
"""
class handleKeys:
    def __init__(self):        
        self.task1_status = False
        self.task2_status = False
        self.temperature_read = False
        self.LDR_read = False 
        self.esc = False      #user wanted to exit the system
    
    def keyInput(self, key):
        if key == ord('l'):
            self.task1_status = True
            self.task2_status = False
            self.temperature_read = False
            self.LDR_read = False 
        elif key == ord('k'):
            self.task1_status = False
        elif key == ord('s'):
            self.task2_status = True
            self.task1_status = False
            self.temperature_read = False
            self.LDR_read = False 
        elif key == ord('a'):
            self.task2_status = False
        elif key == ord('t'):
            self.temperature_read = True
            self.task1_status = False
            self.task2_status = False
            self.LDR_read = False 
        elif key == ord('r'):
            self.temperature_read = False
        elif key == ord('b'):
            self.LDR_read = True
            self.task1_status = False
            self.task2_status = False
            self.temperature_read = False
        elif key == ord('v'):
            self.LDR_read = False
        elif key == 27:
            self.esc = True