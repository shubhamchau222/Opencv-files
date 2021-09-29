import cv2

width = 400   # to set the frame heights and width
height = 400

# if this frame size is not supported to camera specification , then it'll Give You an Error.

cap = cv2.VideoCapture(0)
cap.set(3 , value=width)
cap.set(4,value=height)

while True:
    success , image = cap.read()
    cv2.imshow(winname='webcam-video' , mat=image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break