#Integrantes del Equipo
    # Roberto Valdez Jasso
    # Bruno Sanchez Garcia
    # Carlos Antonio Buendia
    # Maria Araceli Barreto
    # Yasmin Azcona Melendez
#--------------------CODIGO-------------------------
#-------------------IMPORTS--------------------------
import numpy as np
import skimage.measure
import cv2
#----------------------------------------------------

def Max_Pooling(Img):
    Resultado=skimage.measure.block_reduce(Img,(3,3), np.max)
    return Resultado

#Matrix Prueba
#I=[[20,200,-5,23],[-13,134,119,100],[120,32,49,25],[-120,12,9,23]]
#In = np.array(I)
#R=Max_Pooling(In)
#print(R)

#Imagen real
IRGB =cv2.imread('004.jpg')
IGS = cv2.cvtColor(IRGB,cv2.COLOR_BGR2GRAY)
print(IGS.shape)

#funcion real

R2=Max_Pooling(IGS)
print(R2)
print(R2.shape)
cv2.imwrite('004r.jpg',R2)

