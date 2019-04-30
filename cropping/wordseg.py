import cv2
from WordSegmentation import wordSegmentation, prepareImg
def l2wseg(img):
    img=prepareImg(cv2.imread(img),50)
    res = wordSegmentation(img, kernelSize=25, sigma=11, theta=7, minArea=100)
    print("segmented into %d words:"%len(res))
    return res



