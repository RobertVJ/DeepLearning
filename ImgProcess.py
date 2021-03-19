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
cv2.imwrite("MPGS"+Img,Stp2)

