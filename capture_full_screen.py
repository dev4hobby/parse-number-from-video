import cv2
from time import sleep

filename = "play.mp4"
video = cv2.VideoCapture(filename)
count = 0
target_frame = 1
numbers = []

for i in range(target_frame):
  success, image = video.read()
  if not success:
    break
  cv2.imwrite("./docs/images/full-screen.png", image)
