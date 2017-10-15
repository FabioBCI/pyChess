#!/usr/bin/python
#  -*- coding: utf-8 -*-

import pygame
import pygame.camera
import cv2
from pygame.locals import *


class Camera:
    def __init__(self, width=640, height=480):
        # Initialize the webcam
        self.actual_image = []
        self.file_image = []
        self.size = (width, height)
        pygame.camera.init()
        self.cam = pygame.camera.Camera("/dev/video0", self.size)
        self.cam.start()

    def capture_image(self):
        self.actual_image = self.cam.get_image()

    def save_image(self, name_file):
        self.file_image = name_file
        pygame.image.save(self.actual_image, name_file)

    def show_image(self):
        display = pygame.display.set_mode(self.size)
        display.blit(self.actual_image, (0, 0))
        pygame.display.update()

    def delay_camera(self, miliseconds):
        pygame.time.delay(miliseconds)

class CameraCV:
    def __init__(self, width, height):
        self.camera = cv2.VideoCapture(0)
        self.camera.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        self.camera.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

    def capture_frame(self):
        """
        Captures next video frame from camera and returns it
        :return: returns captured frame as NumPy array
        """
        self.camera.open(0)
        rv, self.last_frame = self.camera.read()
        if rv:
            self.camera.release()
            return self.last_frame  # cv2 capture
        else:
            for try_ in range(5):  # Insist on capturing the frame 5 more times if something went wrong
                try:
                    rv_, self.last_frame = self.camera.read()
                    if rv_:
                        self.camera.release()
                        return self.last_frame
                except:  # TODO: Too broad except, should be more specific
                    self.camera.release()
                    pass
            return cv2.error("Error capturing frame.")

    def show_frame(self, frame):
        """
        Method to show a captured frame in an independent CV window
        :return:
        """
        cv2.namedWindow('show-window')
        cv2.imshow('show-window', frame)
        cv2.waitKey(0)
        cv2.destroyWindow("show-window")

    def show_last_frame(self):
        """
        Method to show last captured and stored frame from camera in an independent CV window
        :return:
        """
        cv2.namedWindow('show-window')
        cv2.imshow('show-window', self.last_frame)
        cv2.waitKey(0)
        cv2.destroyWindow("show-window")

    def save_frame(self, frame):
        # TODO: Not implemented yet
        # use imwrite("filename.jpg", img)  # save image
        pass