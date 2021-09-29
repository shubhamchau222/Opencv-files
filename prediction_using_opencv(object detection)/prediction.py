import cv2

thres =  0.65 # threshould to detect the Object

width = 800   #  to set the Frame size of the Oputput window
height = 700

# code for Initializing the webcam
cap = cv2.VideoCapture(0)  # 0 for webcam
cap.set(3 , width )
cap.set(4 , height)
# # cap.set(10,70)


ClassNames = [] # to store the Classes present in the dataset
class_File = 'coco.names'    # class file is required to take the reference
# We'll read the Class_file and copy all the Classes present in class_file into the ClassNames List

# let's copy the class names from class_file to list ClassNames .

with open(class_File , mode='rt') as f :
    ClassNames = f.read().rstrip('\n').split('\n')
    f.close()
#
# print(ClassNames)    # list of all the classNamaes
# print(type(ClassNames))   # class : list


# https://gist.github.com/dkurt/54a8e8b51beb3bd3f770b79e56927bd7
config_path = '.\\ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'  # .pbtxt file
weight_path = '.\\frozen_inference_graph2.pb'      # weights file of trained model


net = cv2.dnn_DetectionModel(weight_path,config_path )
# print(net)
net.setInputScale(1.0/127.0)
net.setInputMean((127.5,127.5,127.5))
net.setInputSize(320 , 320  )
net.setInputSwapRB(True)

while True:
    success , image = cap.read()   # reading the captured Video
    # success => successFully reading or Not , image => image matrix get from Videos

    classIds , Confidence_score , bbox = net.detect(image , confThreshold=thres , nmsThreshold=0.2) # 0.50 => give us three o/p
    #  nmsThreshold=0.2 => for remove the Overlappings from prediction
    print(classIds , Confidence_score , bbox)    # gives the information of classid's

    # if class Id found
    if len(classIds) != 0 :
        for classId , conf_score , box in zip(classIds.flatten() , Confidence_score.flatten() , bbox ):
            # draw rectangle on Image as per Given BBOX matrix
            #cv2.rectangle(image , box , color=(0,255,0 ) , thickness= 2 )   # draw the rectangle on give corresponding to the bbox
            #let's write the name on detected class on Image
            cv2.putText( image , ClassNames[classId - 1].upper() ,
                         (box[0]+10  , box[1]+30)  ,
                         cv2.FONT_HERSHEY_COMPLEX , 1 , (0,255,0) , 2
                         ) #(box[0]+10  , box[1]+30) => location where text need to put (here , slightly above the bbox)

            cv2.putText(image,str(round(conf_score * 100 , 2 )),
                        (box[0] + 200, box[1] + 30),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2
                        )  # (box[0]+10  , box[1]+30) => location where text need to put (here , slightly above the bbox)

    cv2.imshow(winname='Welcome to Object Detection Mania .. ' ,mat= image )
    #cv2.waitKey(1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break














