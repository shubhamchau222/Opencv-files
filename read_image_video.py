import cv2

# How to read the image
im = cv2.imread(filename='jungle7.jpg')
#cv2.imshow(winname='first image' , mat= im ) # display the images
#cv2.waitKey(delay=1000)  # to display image for 10sec
#cv2.waitKey(delay=0) # to display image for infinite time

#------------------------------------------------------------------------------------
''' Display iamge as a Grayscale Image '''

im1 = cv2.imread(filename='jungle7.jpg' , flags=0)  # flags = 0 => for grayscale image
#cv2.imshow(winname='grayscale image ' , mat=im1)
#cv2.waitKey(0)

#------------------------------------------------------------------
'''
        display Image as color image 
'''
im2 = cv2.imread(filename='jungle7.jpg' , flags=1)  # flags = 1 => for colour image
#cv2.imshow(winname='colour image ' , mat=im2)
#cv2.waitKey(0)


#--------------------------------------------------------------------------------------

'''Display Video '''

framewidth = 640     # set the width and height of the frame as per your camera
frameheight = 360

# here we'll Give the recorded video to Display
# To display the webcam video replace this string by 0
cap = cv2.VideoCapture('april21.avi')
cap.set(propId=3 , value=framewidth)  # set the specific frame height and width
cap.set(propId=4 , value=frameheight)   # 4,3 are the by defaults number from opencv

while True :
    success , image = cap.read()  # success => True if video is displaying , else False
    # image = This variable will contains the video frames
    # to display the Video
    cv2.imshow(winname='recorded-video' , mat= image)  # also you can resize here

    # to show video continiously we should provide the delay here
    if cv2.waitKey(1) & 0xFF == ord('q'): # if someone press the 'Q' stop the video
        break

#-------------------------------------------------------------------------------------------------------

cap = cv2.VideoCapture(0)
#cap.set(3 ,50)  # to set the frame size
#cap.set(4,50)   # to set the frame size

while True :
    success , image = cap.read()  # success => True if video is displaying , else False
    # image = This variable will contains the video frames
    # to display the Video
    cv2.imshow(winname='recorded-video' , mat= image)  # also you can resize here

    # to show video continiously we should provide the delay here
    if cv2.waitKey(1) & 0xFF == ord('q'): # if someone press the 'Q' stop the video
        break

#------------------------------------------------------------------------------
