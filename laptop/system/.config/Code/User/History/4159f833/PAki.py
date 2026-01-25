import cv2

pic = "Mii-Face.JPG"

img = cv2.imread(pic, cv2.IMREAD_COLOR)

print(img)