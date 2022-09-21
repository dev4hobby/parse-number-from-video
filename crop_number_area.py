import cv2
from time import sleep

# 영상 캡처(.mp4) 로직 생성

# 영상 불러와서 텍스트 파싱
filename = "play.mp4"
video = cv2.VideoCapture(filename)
count = 0
target_frame = 1
numbers = []

for i in range(target_frame):
  success, image = video.read()
  if not success:
    break
  cropped_rect = image[500:610, 720:1150]
  cv2.imwrite("./docs/images/cropped-number-area.png", cropped_rect)
