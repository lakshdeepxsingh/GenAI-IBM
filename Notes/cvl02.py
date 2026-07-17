import cv2 
import os

detector = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
cv2.namedWindow("Face Detection System",cv2.WINDOW_NORMAL)
cam = cv2.VideoCapture(1)                      # External -> 1 , Internal -> 0
while True:
    rect,frame =cam.read()
    face = detector.detectMultiScale(frame,1.2)
    print(len(face))
    for (x,y,w,h) in face:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,100),3)
    cv2.imshow("Face Detection System",frame)
    if cv2.waitKey(5)==ord("q"):
        break
cam.release()
cv2.destroyAllWindows()


def face_detect(frame):
    detector = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_alt.xml') # loading haarcascade_frontalface_default.xml file
    faces = detector.detectMultiScale(frame, 1.2) # detectMultiScale is used to detect the face in the image
    return faces # return the face detected area in the form of rectangle
    

# GRAY SCALE
def gray_scale(image):
    cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

# CUT FACE

def cut_face(image,face_coord):
    cut_faces=[]
    for (x,y,w,h) in face_coord:
        face=image[y:y+h,x:x+w]
        cut_faces.append(face)
    return cut_faces


# RESIZE

def resize(images,size=(80,100)):
    resized_images=[]
    for image in images:
        img=cv2.resize(image,size)       # we can provide size here but here we are taking default calues only otherwise we cold have written size=(100,100)
        resized_images.append(img)
    return resized_images

# NIRMALIZE INTENSITY

def normalize_intensity(images):
    normalized_faces=[]
    for img in images:
        normalized_faces.append(cv2.equalizeHist(img))
    return normalized_faces

# IMAGE PLOT

import matplotlib.pyplot as plt
def plot(image,title=''):
    plt.figure(figsize=(12,12))
    if image.shape==3:
        cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    plt.imshow(image,c='gray')
    plt.title(title)
    plt.axes("off")
    plt.show()


# PIPELINE

def pipeline(image,face_coord):
    faces = cut_face(image,face_coord)
    faces= resize(faces)
    faces = normalize_intensity(faces)
    return faces

# DRAW RECTANGLE

def draw_ractangle(frame,coords):
    for (x,y,w,h) in coords:
        cv2.rectangle(frame,(x,y),(x+w),(y+h),(0,0,200),2)

# LETS CREATE OUR NEW IMAGE DATASET

name = input("Enter your name: ")
no_Samples = int(input("Enter no of Samples: "))
folder = "dataset/" + name.lower()
if os.path.exists(folder):
    print("Folder with name already exists")
else:
    os.mkdir(folder)
    # To capture pic when press any key
    start_cap = False
    sample=1

    cam = cv2.VideoCapture(1)
    while True:
        rect,frame = cam.read()
        gray = gray_scale(frame)
        coords = face_detect(gray)
        if len(coords)>0:
            faces = pipeline(gray,coords)
            image_name = str(sample)+".jpg"
            cv2.imwrite(img,image_name,0)
        else:
            print("No Face Found !!")
