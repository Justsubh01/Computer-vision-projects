# Import usefull libraries
import cv2 as cv
import numpy as np

# Load the pre-trained classifier
classifier = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

# Load the image
img = cv.imread('./images/groupPhoto.jpg',)
# Resize the image
scaled_img = cv.resize(img,(800,640), cv.INTER_AREA)
# lets detect the faces
face_boxes = classifier.detectMultiScale(scaled_img, 1.24, 1)
# Print the face_boxes with any color
for box in face_boxes:
    # extract the coordinates, height and width
    x, y ,width, height = box
    # lets get other coordinates
    x2, y2 = x + width, y + height
    # lets draw the rectangle 
    cv.rectangle(scaled_img, (x, y), (x2, y2), (0,0,255), 1)


# show the image
cv.imshow('face detection', scaled_img)
# wait until any keyboard argument get pass
cv.waitKey(0)
# close the window
cv.destroyAllWindows()

