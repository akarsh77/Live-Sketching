
import cv2
import numpy as np

def sketch_image(image):
    
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
    
    edge_detected_image = cv2.Canny(blurred_image, 10, 70)

    ret, thresholded_image = cv2.threshold(edge_detected_image, 70, 255, cv2.THRESH_BINARY_INV)

    return thresholded_image

cap = cv2.VideoCapture(0)

while True:
    
    ret, frame = cap.read()
    sketched_image = sketch_image(frame)    
    cv2.imshow('Edge Detected Image', sketched_image)
    
    k = cv2.waitKey(10) & 0xFF
    if k == ord('q') or k == 27:
        break
    
cap.release()
cv2.destroyAllWindows()
