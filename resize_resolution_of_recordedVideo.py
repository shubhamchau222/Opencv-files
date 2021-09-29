import cv2


framewidth = 1080     # set the width and height of the frame as per your camera
frameheight = 1080   # ww can also use it for resizing the videos

# here we'll Give the recorded video to Display
cap = cv2.VideoCapture('april21.avi')

while True :
    success , image = cap.read()  # success => True if video is displaying , else False
    # image = This variable will contains the video frames
    # to display the Video
    image = cv2.resize(image , (framewidth, frameheight))    # resizing Operation
    cv2.imshow(winname='recorded-video' , mat= image)  # also you can resize here

    # to show video continiously we should provide the delay here
    if cv2.waitKey(1) & 0xFF == ord('q'): # if someone press the 'Q' stop the video
        break
