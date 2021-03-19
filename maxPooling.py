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
    Resultado=skimage.measure.block_reduce(Img,(2,2), np.max)
    return Resultado

