import cv2 as cv

# Cascade Classifier
face = cv.CascadeClassifier()

# Load training dataset (will need to change file path)
face.load('faces1.xml')

# Read in image (Will need to chang filepath)
img = cv.imread('sage.jpg')

# Convert image to grayscale and equalize
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
img_gray = cv.equalizeHist(img_gray)

# Find faces
faces = face.detectMultiScale(img_gray)

# Put ellipse around found faces
for (x, y, w, h) in faces:
    center = (x+w//2, y+h//2)
    img = cv.ellipse(img, center, (w//2, h//2), 0, 0, 360, (0, 255, 0), 4)

# Show image with face circled
cv.imshow('Face?', img)

# Wait until key is pressed and close window
cv.waitKey(0)
cv.destroyAllWindows()
