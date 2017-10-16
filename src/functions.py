 #!/usr/bin/python
 # -*- coding: utf-8 -*-
import camera
import cv2

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

