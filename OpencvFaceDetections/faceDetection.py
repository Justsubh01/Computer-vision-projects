# Import usefull libraries
import cv2 as cv
import numpy as np
from PIL import Image
from PIL import ImageTk
from tkinter import filedialog
from tkinter import Label
   
panelA = None
panelB = None

# root = tk.Tk()
# Load the pre-trained classifier
classifier = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

def image_detector():

    # grab a reference to the image panels
    global panelA, panelB
    # Load the pre-trained classifier
    classifier = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
     
    #open a file chooser dailog and allow the user to select an input image
    path = filedialog.askopenfilename()

    if len(path) > 0:
        # Load the image
        img = cv.imread(path)
        # resize normal image
        image = cv.resize(img, (640,480), cv.INTER_AREA)
        # Resize the image
        final_img = cv.resize(img,(640,480), cv.INTER_AREA)
        # lets detect the faces
        face_boxes = classifier.detectMultiScale(final_img, 1.08, 3)
         # Print the face_boxes with any color
        for box in face_boxes:
                # extract the coordinates, height and width
            x, y ,width, height = box
                # lets get other coordinates
            x2, y2 = x + width, y + height
                # lets draw the rectangle 
            cv.rectangle(final_img, (x, y), (x2, y2), (0,255,0), 1)
        
        image = cv.cvtColor(image, cv.COLOR_BGR2RGB)  
        final_image = cv.cvtColor(final_img, cv.COLOR_BGR2RGB)
        # convert the image to PIL format
        image = Image.fromarray(image)
        final_image = Image.fromarray(final_image)


        # convert it to ImageTk format
        image = ImageTk.PhotoImage(image)
        final_image = ImageTk.PhotoImage(final_image)


        # if the panels are None, initialize then
        if  panelA is None or panelB is None:
            # the first panel will shote our original image
            panelA = Label(image=image)
            panelA.image = image
            panelA.pack(side='left', padx=10, pady=10)

            # while the second panel will store the final image map
            panelB = Label(image=final_image)
            panelB.image = final_image
            panelB.pack(side='right', padx=10, pady=10)

        # otherwise update the image panels
        else:
            panelA.configure(image=image)
            panelB.configure(image=final_image)
            panelA.image = image
            panelB.image = final_image #update the panels



