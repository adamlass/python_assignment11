import numpy as np
import cv2
import keyboard
from matplotlib import pyplot as plt 
from skimage.measure import compare_ssim

cap = cv2.VideoCapture(0)

key_frame = []
caption = None
frames_with_object = 0

while(True):

    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    if keyboard.is_pressed('r'):
        key_frame = gray
        print("New Key Frame")

    if len(key_frame) == 0:
        key_frame = gray
    
    cv2.imshow('frame',frame)

    (score, diff) = compare_ssim(key_frame, gray, full=True)
    if score <= 0.85:
        frames_with_object += 1
        print(score)
        if frames_with_object == 24*3:
            caption = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            plt.imshow(caption)
            plt.show()
    else:
        frames_with_object = 0
        print("No picture") 


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
