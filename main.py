import cv2
import os

# Load the cascade classifier for face detection
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Read the video file
video = cv2.VideoCapture("video.mp4")

# Create a folder to save the detected faces
if not os.path.exists("faces"):
    os.makedirs("faces")

# Loop through each frame in the video
frame_count = 0
while True:
    ret, frame = video.read()
    if not ret:
        break

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # Loop through each detected face
    for (x, y, w, h) in faces:
        # Filter the faces to be in the desired dimensions
        if w > 100 and h > 100:
            face_frame = frame[y:y + h, x:x + w]
            face_gray = gray[y:y + h, x:x + w]

            # Save the face in the folder
            face_file = "faces/face_{}.png".format(frame_count)
            cv2.imwrite(face_file, face_gray)
            frame_count += 1

# Release the video file
video.release()
