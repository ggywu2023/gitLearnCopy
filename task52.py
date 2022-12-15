import cv2

img = cv2.imread('sample29_cut.jpg')
# covert to gray image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# get a binary image
ret, thresh = cv2.threshold(gray, 220, 255, 0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
# draw the contour of line
imgnew = cv2.drawContours(img, contours[4], -1, (255, 0, 0), 1)
print(len(contours))
cnt = contours[4]
# count the length
perimeter = cv2.arcLength(cnt, False)
print('length:', perimeter)
area = cv2.contourArea(cnt)
print('area:', area)
width = area / perimeter
print('width:', width)

cv2.namedWindow("imgshow", 1)
cv2.imshow("imgshow", imgnew)

cv2.waitKey()
