 #!/usr/bin/python
 # -*- coding: utf-8 -*-
import camera
import pygame
from argparse import ArgumentParser
import functions as fs


def main(options):
	#This program capture one image each 1 second

	cam=camera.camera(options.wt,options.ht)
	cam.capture_image()
	anterior_image=cam.actual_image

	while True:
		cam.capture_image()
		cam.save_image('./prof1.png')
		fs.save_image('./prof2.png',anterior_image)
		anterior_image=cam.actual_image

		imr=fs.differences_images('./prof1.png','./prof2.png')
		fs.save_cv2_image('./result.png',imr)
		imr = pygame.image.load('./result.png')
		cam.image_show=imr
		cam.show_image()

		#cam.show_image()
		cam.delay_camera(options.time)



if __name__ == '__main__':
	argp=ArgumentParser(version='1.0',description='Program for automatic algebraic annotation of a game chess',epilog='Copyright 2017 Autor under license MIT')	
	argp.add_argument('-t',help='Time in miliseconds that capture images',dest='time',required='False',type=int)
	argp.add_argument('-wt',help='Weight of the image',dest='wt',type=int)
	argp.add_argument('-ht',help='Height of the image',dest='ht',type=int)
	opts = argp.parse_args()
	main(opts)