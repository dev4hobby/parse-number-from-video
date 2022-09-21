import cv2
from time import sleep

# 영상 캡처(.mp4) 로직 생성

# 영상 불러와서 텍스트 파싱
filename = "play.mp4"
video = cv2.VideoCapture(filename)
count = 0
numbers = []

while True:
  success, image = video.read()
  if not success:
    break
  cv2.rectangle(image, (720, 500), (820, 610), (0, 255, 0), 2)
  cv2.rectangle(image, (830, 500), (910, 610), (0, 255, 0), 2)
  cv2.rectangle(image, (915, 500), (990, 610), (0, 255, 0), 2)
  cv2.rectangle(image, (1000, 500), (1070, 610), (0, 255, 0), 2)
  cv2.rectangle(image, (1075, 500), (1180, 610), (0, 255, 0), 2)
  
  # show image on screen
  cv2.imwrite("./docs/images/numbers-area.png".format(count), image)
  sleep(0.5)