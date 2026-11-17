import cv2

# load pre trained model file
face_cascade = cv2.CascadeClassifier("images/haarcascade_frontalface_default.xml")

# read image to numpy array 
img = cv2.imread("ownself.jpg")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# convert image to gray scale
# detect faces in image
faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.05, minNeighbors=5)
# loop through coordinates of face
# draw rectangle where face has been detected
for x, y, w, h in faces:
    img=cv2.rectangle(img, (x, y),(x+w, y+h),(0,255, 0), 3)
# print numpy array coordinates
print(type(faces))
print(faces)
# resize image
resized = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))
# show new image
cv2.imshow("Gray", resized)
# wait till key pressed
cv2.waitKey(0)
# close all windows
cv2.destroyAllWindows()