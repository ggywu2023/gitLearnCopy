import cv2

img = cv2.imread('sample10.jpg')
# covert to gray image
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# get a binary image
res, dst = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)

contours, hierarchy = cv2.findContours(dst,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

# count the grain
count = 0

color = 120
for cont in contours:
    # caculate the area
    ares = cv2.contourArea(cont)
    # filter the area, which is less 50
    if ares < 50:
        continue
    # count the grain +1
    count += 1
    # draw the grain with different color
    cv2.drawContours(img, [cont], -1, (255, color, 0), -1)
    color += 5

print("number of grains:", count)

cv2.namedWindow("imgshow", 1)
cv2.imshow('imgshow', img)

cv2.namedWindow("dst", 2)
cv2.imshow("dst", dst)

cv2.waitKey()