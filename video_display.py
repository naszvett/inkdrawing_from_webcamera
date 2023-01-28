import cv2 as cv
import video_stream as vs
import numpy as np


class Editors:
    def gray(img):
        return cv.cvtColor(img, cv.COLOR_BGR2GRAY)


    def gauss(img):
        return cv.GaussianBlur(img, (3, 3), 0)


    def adaptive_treshold(img):
        return cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C,\
                cv.THRESH_BINARY,15,2)


    def sharpen(img):
        kernel = np.array([[0, -1, 0],
                                [-1, 5, -1],
                                [0, -1, 0]])
        return cv.filter2D(src=img, ddepth=-1, kernel=kernel)


    def erode(img):
        return cv.erode(img, None, iterations=1)

class DisplayVideo:
    def __init__(self, src=0):
        self.video_getter = vs.VideoGet(src)
        self.video_shower = vs.VideoShow(self.video_getter.frame)
        self.start = self.start
        self.editors = None

    def start(self):
        self.video_getter.start()
        self.video_shower.start()
        while True:
            if self.video_getter.stopped or self.video_shower.stopped:
                self.video_shower.stop()
                self.video_getter.stop()
                break

            frame = self.video_getter.frame
            try:
                for editor in self.editors:
                    frame = editor(frame)
            except TypeError:
                pass
            self.video_shower.frame = frame
