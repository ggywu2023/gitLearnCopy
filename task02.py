import cv2
import numpy as np


def calc_coordinate_area(contour):
    M = cv2.moments(contour)  # 计算轮廓的各阶矩,字典
    # print(M)
    # 计算重心
    cx = int(M['m10'] / M['m00'])
    cy = int(M['m01'] / M['m00'])
    # 计算轮廓面积
    area = cv2.contourArea(contour)
    print('cx:%f, cy:%f, area:%f' % (cx, cy, area))
    return cx, cy, area


def main():
    img0 = cv2.imread('sample29_cut.jpg')
    img = img0.copy()

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    img = cv2.dilate(img, kernel, iterations=1)

    ret, thresh = cv2.threshold(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), 127, 255, 0)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)  # 得到轮廓信息
    print(len(contours))

    areas = []
    coordinate = []
    for i in range(len(contours)):
        cx, cy, area = calc_coordinate_area(contours[i])
        areas.append(area)
        coordinate.append([cx, cy])
    print(areas)
    areas_np = np.array(areas)
    max_idx = np.argmax(areas_np)  # 得到最长路径索引
    min_idx = np.argmin(areas_np)  # 得到最短路径索引
    print("max: %d, min: %d" % (max_idx, min_idx))
    imgnew = cv2.drawContours(img, contours[max_idx], -1, (0, 255, 0), 1)  # 画出最长路径
    imgnew = cv2.drawContours(imgnew, contours[min_idx], -1, (0, 0, 255), 1)  # 画出最段路径
    print(coordinate[max_idx]) # 最长路径重心坐标
    print(coordinate[min_idx]) # 最短路径重心坐标
    cv2.circle(imgnew, tuple(coordinate[max_idx]), 3, (0, 255, 0), 3)  # 画出最长路径重心坐标
    cv2.circle(imgnew, tuple(coordinate[min_idx]), 3, (0, 0, 255), 3)  # 画出最短路径重心坐标

    cv2.imshow('img0', img0)
    # cv2.imshow('thresh', thresh)
    cv2.imshow('imgnew', imgnew)
    cv2.imwrite('imgnew_result.jpg', imgnew)
    cv2.waitKey(0)


if __name__ == '__main__':
    main()
