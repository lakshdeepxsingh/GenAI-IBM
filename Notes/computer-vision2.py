# pip install opencv-python

import cv2
cam = cv2.VideoCapture(0)          # 0 -> internal , 1 -> external
rect,frame = cam.read()  # rect - check if any obj infront of camera and frame - catures imagae infront of cam 
cv2.waitKey(5)          # Delay time
cam.release()                   # To release the camera
cv2.destroyAllWindows()         

print(rect)             # prints if object present present or not

print(frame)            # prints image present infront of camera

import matplotlib.pyplot as plt
plt.imshow(frame)          # to show captured image 
plt.show()  

'''
cv2.namedWindow("Video Capturing",cv2.WINDOW_NORMAL)
cam = cv2.VideoCapture(1)
while True :
    rect,frame = cam.read()
    cv2.imshow("Video Capturing",frame)

    if cv2.waitkey(5)==ord("q"):
        break

cam.release()
cv2.destroyAllWindows()

'''

'''
for android ...install droidCam on both devices and connect them through wifi


'''