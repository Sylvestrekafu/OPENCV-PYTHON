import numpy as np
import cv2

cap = cv2.VideoCapture(0)



while (True):
    ret, frame = cap.read()



    cv2.imshow('frame', frame)
    k = cv2.waitKey(30) & 0xff
    if k == 27: # press ESP po echap button
        break

cap.release()
cv2.destroyAllWindows()