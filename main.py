import cv2
filePath = 'dinoo.jpg'
imgFlag = int(1)
img = cv2.imread(filePath,imgFlag)
cv2.imshow("Baby Dinosaur",img)
cv2.waitKey(0)
cv2.destroyAllWindows()