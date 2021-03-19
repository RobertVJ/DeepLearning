#Integrantes del Equipo
# Roberto Valdez Jasso
# Bruno Sanchez Garcia
# Carlos Antonio Buendia
# Maria Araceli Barreto
# Yasmin Azcona Melendez
#--------------------CODIGO-------------------------

import numpy as np
import cv2
from  convolucion import convolucion, conv_GS
from  maxPooling import Max_Pooling

#Step1
Img = input("Inserte nombre y extención del archivo: ")
Stp1 = conv_GS(Img)
print (Stp1.shape)
#Step2 
Stp2 = Max_Pooling(Stp1)
print(Stp2.shape)
#Step3
Kernel2=np.array([[2,2,4,2,2],[1,1,2,1,1],[0,0,0,0,0],[-1,-1,-2,-1,-1],[-2,-2,-4,-2,-2]])
Stp3 = convolucion(Stp2,Kernel2)
print(Stp3.shape)
#Step4
Stp4 = Max_Pooling(Stp3)
print(Stp4.shape)
cv2.imwrite("MPGS"+Img,Stp4)

