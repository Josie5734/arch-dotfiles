import cv2

pic = "pretty.jpg"

bob = cv2.imread(pic, cv2.IMREAD_COLOR)

img = cv2.Canny(bob,100,200)

cv2.imshow("Mii",img)
cv2.waitKey(0)
cv2.destroyAllWindows()