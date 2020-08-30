# open cv is a library for image recognition. cv2 allows you to read an image
import cv2
import face_recognition

# take user's image and get 128D facial points
def make_vector(imageFile):
    # get image from user through api
    image = cv2.imread(imageFile)
    # get image colors
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # based on colors, detect face
    boxes = face_recognition.face_locations(rgb, model="hog")
    # using box, get encodings of face
    # data format called an MD array, type of python array
    encodings = face_recognition.face_encodings(rgb, boxes)
    return encodings
