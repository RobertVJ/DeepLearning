import numpy as np
import cv2

def convolucion(Ioriginal,Kernel):
    fr=len(Ioriginal)-(len(Kernel)-1)
    cr=len(Ioriginal[0])-(len(Kernel[0])-1)
    Resultado=np.zeros((fr,cr),np.uint8)
    #For para recorrer filas
    for i in range(len(Resultado)):
        #For para recorrer columnas
        for j in range(len(Resultado[0])):
            suma=0
            #hace las multiplicaciones y las suma
            for m in range(len(Kernel)):
                for n in range(len(Kernel[0])):
                    suma+=Kernel[m][n]*Ioriginal[m+i][n+j]
            if suma<=255:        
                Resultado[i][j]=round(suma)
            else:
                Resultado[i][j]=255
    return Resultado
def conv_GS(Img):

    #Kernel
    K=[[-1,0,1],[-1,0,1],[-1,0,1]]

    #imagenes a numpy arrays
    Kn=np.array(K)
    IRGB=cv2.imread(Img)
    IGS=cv2.cvtColor(IRGB,cv2.COLOR_BGR2GRAY)

    #funcion de convolucion
    return convolucion(IGS,Kn)
cv2.imwrite("004GS.jpg",conv_GS("004.jpg"))

