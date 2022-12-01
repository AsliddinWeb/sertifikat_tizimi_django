import os
import cv2
from PIL import ImageFont

list_of_names = []


def delete_old_data():
   for i in os.listdir("generated-certificates/"):
      os.remove("generated-certificates/{}".format(i))


def cleanup_data():
   with open('name-data.txt') as f:
      for line in f:
          list_of_names.append(line.strip())


def sertifikat(name):
   image = cv2.imread("new_template.jpg")

   textSize = list(cv2.getTextSize(name, cv2.FONT_HERSHEY_COMPLEX, 0.5, 2))[0][0]
   textSize2 = list(cv2.getTextSize(name, cv2.FONT_HERSHEY_COMPLEX, 0.5, 2))[0][1]

   print(cv2.getTextSize(name, cv2.FONT_HERSHEY_COMPLEX, 1, 1))


   a = int(image.shape[1]/2) - int(textSize*3) - int(textSize2*8)
   b = int(image.shape[0]/2)

   cv2.putText(
      img = image,
      text = name.strip(),
      org = (a, b),
      # fontFace=ImageFont.truetype("./Roboto-Italic.ttf", 40),
      fontFace = cv2.FONT_ITALIC,
      fontScale = 4,
      color = (0, 0, 0),
      thickness = 10,
      lineType = cv2.LINE_AA
   )
   cv2.imwrite("generated-certificates/{}.jpg".format(name.strip()), image)
   print(f"Processing finished: {name}")

def main(name):
   sertifikat(name)
