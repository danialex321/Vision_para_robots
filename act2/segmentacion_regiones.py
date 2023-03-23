# Programa para segmentar regiones de interés en función del color
import cv2
import numpy as np

if __name__ == '__main__':
    print("Inicio")
    # Abrimos la imagen
    img = cv2.imread("im2.jpeg");
    print(img.shape)
    # Cambiamos de tamaño (opcional)
    f=0.5
    img_resized=cv2.resize(img, (0,0), fx=0.5, fy=0.5)

    # Cambiamos de espacio de color (¿cuál espacio nos conviene?)
    x_ini=900
    y_ini=1120
    s_ini=10
    sample =img_resized[int(y_ini*f):int(y_ini*f + s_ini),int(x_ini*f):int(x_ini*f + s_ini),:]
    #print(sample)
    min_sample=np.min(sample,axis=(0,1))
    max_sample=np.max(sample,axis=(0,1))
    print("minimo:",min_sample)
    print("maximo:",max_sample)


    # Umbralizamos
    img_bin=cv2.inRange(img_resized, (75,160,245),(90,175,260))

    kernel = np.ones ((5,5),np.uint8)
    img_closed=cv2.morphologyEx(img_bin,cv2.MORPH_CLOSE,kernel)

    # Buscamos contornos
    contours, hierch= cv2.findContours(img_closed, cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    # Dibujamos contornos

    # Guardamos resultado
    #cv2.imshow("img",img)
    cv2.imshow("img_resized", img_resized)
    cv2.imshow("img_bin", img_bin)
    cv2.imshow("img_closed", img_closed)
    #    cv2.imshow("img_bin", img_bin)

    cv2.waitKey(0)
