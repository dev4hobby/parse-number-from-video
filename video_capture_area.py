import cv2
import pyautogui
import numpy as np

frames = []
width = 1920
height = 1080

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video = cv2.VideoWriter('video.mp4', fourcc, 1, (width, height))

for i in range(60):
  print(f"frame_count >> {i}")
  pic = pyautogui.screenshot(region=(0, 0, width, height))
  image_frame = np.array(pic)
  image_frame = cv2.cvtColor(image_frame, cv2.COLOR_BGR2RGB)
  frames.append(image_frame)

for frame in frames:
  video.write(frame)

cv2.destroyAllWindows()
video.release()