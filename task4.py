import cv2 as cv
import numpy as np

img = cv.imread("sample_ship.png")
img_p = img.copy()

# covert to gray image
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

_, binary = cv.threshold(gray, 0, 255, cv.THRESH_OTSU)

gussimage = cv.GaussianBlur(gray, (5,5), 0)

# edges detection with Canny method
edges = cv.Canny(gussimage, threshold1=100, threshold2=200)

# using HoughLinesP
lines_p = cv.HoughLinesP(edges, rho = 1, theta = np.pi/180, threshold = 100, minLineLength= 40, maxLineGap=10)

for i in range(len(lines_p)):
    x_1, y_1, x_2, y_2 = lines_p[i][0]
    cv.line(img_p, (x_1, y_1), (x_2, y_2), (0, 255, 0), 2)

cv.namedWindow("Hough_line_p", 2)
cv.imshow("Hough_line_p", img_p)

cv.waitKey(0)
