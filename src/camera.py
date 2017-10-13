 #!/usr/bin/python
 # -*- coding: utf-8 -*-

import pygame
import pygame.camera
from pygame.locals import *


class camera:

 	def __init__(self,weight,height):
 		#Inicialize the webcam
 		self.size = (weight,height)
		pygame.camera.init()	
		self.cam = pygame.camera.Camera("/dev/video0",self.size)	
		self.cam.start()

	def capture_image(self):
		self.actual_image=self.cam.get_image()

	def save_image(self,name_file):
		pygame.ima.save_image(self.actual_image,name_file)

	def show_image(self):
		display=pygame.display.set_mode(self.size)
		display.blit(self.actual_image,(0,0))
		pygame.display.update()

