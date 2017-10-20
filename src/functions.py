 #!/usr/bin/python
 # -*- coding: utf-8 -*-
import pygame
import numpy as np
import pygame.camera
import camera
import cv2



def show_image(image):
		cv2.imshow(" ",image)
		cv2.waitKey(0)
		cv2.destroyAllWindows()

def save_image(name_file,im):
	pygame.image.save(im,name_file)

def save_cv2_image(name_file,im):
	cv2.imwrite(name_file,im)

def detect_corners(image):
	#En esta funcion detectamos los contornos de la imagen
	#Creo que podria servir para detectar el contorno externo que seria el del tablero

	img=cv2.imread(image)
	gris=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #Conversion a escala de grises
	gaussian=cv2.GaussianBlur(gris,(5,5),0) #Realizamos un suavizado de la imagen
	canny=cv2.Canny(gaussian,50,150)
	(_,contornos,_)=cv2.findContours(canny.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
	cv2.drawContours(img,contornos,-1,(0,0,255),2)
	cv2.imshow("contornos",img)
	if cv2.waitKey(): cv2.destroyAllWindows()


def differences_images(image1,image2):
	diff1=cv2.imread(image1) #Read the file that contain the image 1
	diff2=cv2.imread(image2) 

	diff_total = cv2.absdiff(diff1, diff2)
	imagen_gris = cv2.cvtColor(diff_total, cv2.COLOR_BGR2GRAY)
	(_,contours,_)= cv2.findContours(imagen_gris,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

	for c in contours:
			if cv2.contourArea(c) >= 1:
				posicion_x,posicion_y,ancho,alto = cv2.boundingRect(c) #Guardamos las dimensiones de la Bounding Box
				cv2.rectangle(diff1,(posicion_x,posicion_y),(posicion_x+ancho,posicion_y+alto),(0,0,255),1) #Dibujamos la bounding box sobre diff1
	return diff_total

def trigger_cam(image1):
	#Esta funcion nos indica si esta habiendo un cambio en la imagen
	#Basicamente miro si existen muchos pixeles blancos, eso significa que estoy pasando la mano
	#Por la webcam
	im=cv2.imread(image1)
	gray1=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
	binary1 = cv2.adaptiveThreshold(gray1, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)

	cont=0
	size=np.shape(binary1)
	for i in range(0,size[0]):
		for j in range(0,size[1]):
			if(binary1[i,j]==0):
				cont=cont+1
			else:
				pass
		

	if(cont>250):
		print(True)
		return True
	else:
		print(False)
		return False

