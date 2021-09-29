import cv2

im = cv2.imread(filename='jungle7.jpg')
cv2.imshow(winname='jungle 1 Original image ' , mat=im)
cv2.waitKey(0)


#--------------------------
# Image Resizing
height = 1080
width = 1080

im1 = cv2.imread(filename='jungle7.jpg')
im1 = cv2.resize(im1 , (width , height ))   # resizing Operation
cv2.imshow(winname='jungle 1 Resized Image ' , mat=im1)
cv2.waitKey(0)


#-----------------------------------------------
# Grayscale Image

im2 = cv2.imread(filename='jungle7.jpg' ,  flags=0)  # flags=0 ( grayscale Image )
cv2.imshow(winname='jungle 1 GrayScale  Image ' , mat=im2)
cv2.waitKey(0)


#--------------------------------------------------------
# another Technique OF changing Color Scheme

im3 = cv2.imread(filename='jungle7.jpg' )  # flags=0 ( grayscale Image )
gray_img = cv2.cvtColor(im3 ,cv2.COLOR_BGR2GRAY)
cv2.imshow(winname='jungle Another GrayScale  Image ' , mat=gray_img)
cv2.waitKey(0)


#------------------------------------------------------------------
# Changing the Color Scheme
# BGR => RGBq

im4 = cv2.imread(filename='jungle7.jpg' )  # flags=0 ( grayscale Image )
im4 = cv2.resize(im4 , (1080,1080))
RGB_image  = cv2.cvtColor(im4 ,cv2.COLOR_BGR2RGB)
cv2.imshow(winname='jungle BGR=> RGB  Image ' , mat=RGB_image)
cv2.waitKey(0)

#---------------------------------------------------------------------------
# Changing the Color Scheme
#COLOR_HSV2RGB_FULL

im5 = cv2.imread(filename='jungle7.jpg' )  # flags=0 ( grayscale Image )
im5 = cv2.resize(im5 , (1080,1080))
COLOR_HSV2RGB_FULL  = cv2.cvtColor(im5 ,cv2.COLOR_HSV2RGB_FULL)
cv2.imshow(winname='jungle COLOR_HSV2RGB_FULL  Image ' , mat=COLOR_HSV2RGB_FULL)
cv2.waitKey(0)


#------------------------------------------------------------------------------
# Changing the Color Scheme
#BGR

im6 = cv2.imread(filename='jungle7.jpg' )  # flags=0 ( grayscale Image )
im6 = cv2.resize(im6 , (1080,1080))
COLOR_HSV2RGB_FULL  = cv2.cvtColor(im6 ,cv2.COLOR_HSV2RGB_FULL)
cv2.imshow(winname='jungle COLOR_HSV2RGB_FULL  Image ' , mat=COLOR_HSV2RGB_FULL)
cv2.waitKey(0)



#----------------------------------------------------------------------------
#Blure IMages

im7 = cv2.imread(filename='jungle7.jpg' )  # flags=0 ( grayscale Image )
im7 = cv2.resize(im7 , (1080,1080))
Blur_image = cv2.GaussianBlur(im7 ,(7,7),0 )
cv2.imshow(winname='Blurr  Image ' , mat=Blur_image)
cv2.waitKey(0)


#-----------------------------------------------
#canny
im8 = cv2.imread(filename='jungle7.jpg' )  # flags=0 ( grayscale Image )
im8 = cv2.resize(im8 , (1080,1080))
# Blur_image = cv2.GaussianBlur(im7 ,(7,7),0 )
im8 = cv2.Canny(im8 , 100 ,200 )
cv2.imshow(winname='Canny Image ' , mat=im8)
cv2.waitKey(0)










