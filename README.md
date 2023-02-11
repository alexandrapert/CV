# CV
Face saver from videos


# 1. Introduction

This face saver is written using Python with the OpenCV library that reads an mp4 video file  imported from a youtuber and detects faces from each frame. The faces are filtered to be within a certain size, and then saved in a separate folder.


# 2. Applications

This code can be used in various computer vision applications such as face recognition, video surveillance, and security systems.


# 3. Algorithm Steps

The algorithm follows these steps:

Load the cascade classifier for face detection using the OpenCV's cv2.CascadeClassifier class.
Read the mp4 video file using the cv2.VideoCapture class.
Create a folder to store the detected faces if it doesn't already exist.
Loop through each frame of the video and convert it to grayscale using the cv2.cvtColor function.
Use the detectMultiScale method of the cv2.CascadeClassifier class to detect faces in the grayscale frame.
Filter the detected faces to only include those with dimensions greater than 100x100.
Save the filtered faces in the created folder using the cv2.imwrite function.
Release the video file using the VideoCapture.release method.

# 5. Implementation

The code uses the OpenCV library for face detection, grayscale conversion, and image writing. The Haar cascade XML file haarcascade_frontalface_default.xml is used for face detection.


# 6. Usages

This code can be used as a starting point for various computer vision projects that involve face detection and extraction from videos. It can also be modified to perform face detection on other types of videos or images.


# 7. Conclusion

In conclusion, this code provides a simple implementation of face detection and extraction from a video using the OpenCV library in Python. The extracted faces can be used for further analysis or processing in various computer vision applications.

