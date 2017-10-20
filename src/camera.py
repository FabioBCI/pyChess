 #!/usr/bin/python
 # -*- coding: utf-8 -*-

import pygame
import pygame.camera
import cv2
from pygame.locals import *


class camera:

 	def __init__(self,weight,height):
 		#Inicialize the webcam
 		self.actual_image=[]
 		self.file_image=[]
 		self.size = (weight,height)
		pygame.camera.init()	
		self.cam = pygame.camera.Camera("/dev/video0",self.size)	
		self.cam.start()
		self.image_show=[]

	def capture_image(self):
		self.actual_image=self.cam.get_image()

	def save_image(self,name_file):
		self.file_image=name_file
		pygame.image.save(self.actual_image,name_file)

	def show_image(self):
		display=pygame.display.set_mode(self.size)
		display.blit(self.image_show,(0,0))
		pygame.display.update()

	def delay_camera(self,miliseconds):
		pygame.time.delay(miliseconds)
