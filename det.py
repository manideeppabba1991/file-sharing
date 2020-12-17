# -*- coding: utf-8 -*-
#!/usr/bin/python

import os
import cv2 as cv
import numpy as np

class Detector():
    def __init__(self, proto, param, thres):
        self.model = cv.text.TextDetectorCNN_create(proto, param)
        self.thres = thres
   
    def get_box(self, img):
        res = []
        rects, outProbs = self.model.detect(img)
        for r in range(np.shape(rects)[0]):
            if outProbs[r] > self.thres:
                rect = rects[r]
                res.append(rect)
        return res
    
    def draw_and_write(self, img, name):
        rects, outProbs = self.model.detect(img)
        for r in range(np.shape(rects)[0]):
            if outProbs[r] > self.thres:
                rect = rects[r]
                cv.rectangle(img, (rect[0],rect[1]), (rect[0] + rect[2], rect[1] + rect[3]), (255, 0, 0), 2)
        cv.imwrite(name, img)

if __name__ == "__main__":
    path = "image sample path"
    os.chdir(path)
    detector = Detector("network.prototxt", "TextBoxes_icdar13.caffemodel", 0.6)
    img = cv.imread("temp96_4.jpg")
    detector.get_box(img)
    detector.draw_and_write(img,"test.jpg")
        
                