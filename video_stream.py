import cv2 as cv
from threading import Thread
from datetime import datetime

class VideoGet:
    def __init__(self, src=0):
        self.stream = cv.VideoCapture(src)
        (self.grabbed, self.frame) = self.stream.read()
        self.stopped = False

    def start(self):
        Thread(target=self.get, args=()).start()
        return self

    def get(self):
        while not self.stopped:
            if not self.grabbed:
                self.stop()
            else:
                (self.grabbed, self.frame) = self.stream.read()

    def stop(self):
        self.stopped = True


class VideoShow:
    def __init__(self, frame=None):
        self.frame = frame
        self.stopped = False

    def start(self):
        Thread(target=self.show, args=()).start()
        return self

    def show(self):
        while not self.stopped:
            cv.imshow("Video", self.frame)
            key = cv.waitKey(1)
            if key == ord("q"):
                self.stopped = True
            elif key == ord("s"):
                fileformat = "png"
                time = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename =f"image_{time}.{fileformat}"
                cv.imwrite(filename, self.frame)

    def stop(self):
        self.stopped = True

class DisplayVideo:
    def __init__(self, src=0):
        self.video_getter = VideoGet(src)
        self.video_shower = VideoShow(self.video_getter.frame)
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
