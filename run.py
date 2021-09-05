import cv2

with open('name-data.txt') as f:
   for line in f:
       img = cv2.imread("certificate-template.jpg")
       cv2.imwrite("{}.jpg".format(line.strip()), img)
       print(line.strip())


