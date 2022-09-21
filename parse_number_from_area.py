import cv2
from time import sleep
from pytesseract import image_to_string
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor

numbers = defaultdict(list)

def get_number_from_image_area(image_area):
  text_info = image_to_string(
    image_area,
    lang='eng',
    config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789',
  )
  return text_info


def append_number_to_dict(image_areas_with_index):
  image_area, index = image_areas_with_index
  number = get_number_from_image_area(image_area)
  if not number:
    return
  numbers[index].append(int(number))

def most_frequent(data):
    return max(data, key=data.count)

def check_number():
  result = []
  for i in range(1, 6):
    number_set = list(set(numbers[i]))
    if len(number_set) == 0:
      continue
    if len(number_set) == 1:
      result.append(number_set[0])
    else:
      number = most_frequent(numbers[i])
      result.append(number)
  
  print("result >> ", result)
  result = ''.join([str(_) for _ in result])

  if len(result) == 5:
    return result, True
  return result, False

def get_answer_from_video(filename):
  video = cv2.VideoCapture(filename)
  count = 0
  threshold = 10

  while True:
    success, image = video.read()
    if not success:
      break
    
    image_areas_with_index = [
      [image[500:610, 720:820], 1],
      [image[500:610, 830:910], 2],
      [image[500:610, 915:990], 3],
      [image[500:610, 1000:1070], 4],
      [image[500:610, 1075:1180], 5],
    ]

    with ThreadPoolExecutor(max_workers=5) as pool:
      pool.map(append_number_to_dict, image_areas_with_index)
    sleep(0.5)
    print("Numbers", numbers)
    count += 1
    if count % threshold == 0:
      result, okay = check_number()
      if not okay:
        continue
      break
  
  return result


if __name__ == "__main__":
  filename = "play.mp4"
  result = get_answer_from_video(filename)
  print("result >> ", result)