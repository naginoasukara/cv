import numpy as np
import cv2

#pic_dir = '/home/evga/rxy/color_test/gen_color_pic/'
pic_dir = 'C:\\Users\\renxinyuan\\Desktop\\color_test\\gen_color_pic\\'

def create_image_black():
    img = np.zeros([400, 400, 3], np.uint8)
    #cv2.imshow("iamge", img)
    #cv2.waitKey(0)
    cv2.imwrite(pic_dir + 'black.jpg', img)

create_image_black()

def create_image_white():
    img = np.zeros([400, 400, 3], np.uint8)
    img[:, :, 0] = np.zeros([400, 400]) + 255
    img[:, :, 1] = np.ones([400, 400]) + 254
    img[:, :, 2] = np.ones([400, 400]) * 255
    #cv2.imshow("iamge", img)
    img2 = np.zeros([400, 400, 3], np.uint8)+255
    #cv2.imshow("iamge2", img2)
    #cv2.waitKey(0)
    cv2.imwrite(pic_dir + 'white.jpg', img)

create_image_white()

def create_image_gbry():
    img_blue = np.zeros([400, 400, 3], np.uint8)
    img_blue[:, :, 0] = np.zeros([400, 400]) + 255
    #print img_blue
    #cv2.imshow("iamge_blue", img_blue)
    cv2.imwrite(pic_dir + 'blue.jpg', img_blue)
    img_green = np.zeros([400, 400, 3], np.uint8)
    img_green[:, :, 1] = np.zeros([400, 400]) + 255
    #cv2.imshow("iamge_green", img_green)
    cv2.imwrite(pic_dir + 'green.jpg', img_green)
    img_red = np.zeros([400, 400, 3], np.uint8)
    img_red[:, :, 2] = np.zeros([400, 400])+ 255
    #cv2.imshow("iamge_red", img_red)
    #cv2.waitKey(0)
    cv2.imwrite(pic_dir + 'red.jpg', img_red)
    img_yellow = np.zeros([400, 400, 3], np.uint8)
    img_yellow[:, :, 2] = np.zeros([400, 400]) + 255
    img_yellow[:, :, 1] = np.zeros([400, 400]) + 255
    #cv2.imshow("iamge_yellow", img_yellow)
    #cv2.waitKey(0)
    cv2.imwrite(pic_dir + 'yellow.jpg', img_yellow)
    img_cyan = np.zeros([400, 400, 3], np.uint8)
    img_cyan[:, :, 0] = np.zeros([400, 400]) + 255
    img_cyan[:, :, 1] = np.zeros([400, 400]) + 255
    #cv2.imshow("iamge_cyan", img_cyan)
    #cv2.waitKey(0)
    cv2.imwrite(pic_dir + 'cyan.jpg', img_cyan)

create_image_gbry()


