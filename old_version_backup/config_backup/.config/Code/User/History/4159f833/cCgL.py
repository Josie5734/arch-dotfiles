import cv2

pic = "Mii-Face.JPG"

bob = cv2.imread(pic, cv2.IMREAD_COLOR)

img = cv2.Canny(bob,100,100)

cv2.imshow("Mii",img)
cv2.waitKey(0)
cv2.destroyAllWindows()