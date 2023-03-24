# Programa para segmentar regiones de interés en función del color
import cv2
import numpy as np

if __name__ == '__main__':
    print("Inicio")
    # Abrimos la imagen
    img = cv2.imread("im3.jpeg")
    print(img.shape)

    # Cambiamos de tamaño (opcional)
    f = 0.5
    img_resized = cv2.resize(img, (0,0), fx=f, fy=f)

    # Tomamos una muestra de la región de interés
    min_sample =  (88, 218, 137)
    max_sample =  (119,245,167)
    
    print("minimo: ", min_sample)
    print("maximo: ", max_sample)

    # Umbralizamos
    img_bin = cv2.inRange(img_resized, min_sample, max_sample)

    # Limpiamos ruido en la imagen
    kernel = np.ones((5,5), np.uint8)
    img_closed = cv2.morphologyEx(img_bin, cv2.MORPH_CLOSE, kernel)

    # Buscamos contornos
    contours, hier = cv2.findContours(img_closed, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    #print(contours)
    #print(hier)

    # Dibujamos contornos
    img_cnts = cv2.drawContours(img_resized, contours, -1, (0,0,255), 2)

    #cv2.imshow("img", img)
    cv2.imshow("img_resized", img_resized)
    cv2.imshow("img_bin", img_bin)
    cv2.imshow("img_closed", img_closed)
    cv2.imshow("contours", img_cnts)
    cv2.waitKey(0)

    # Guardamos resultado
    cv2.imwrite("resultado.png", img_cnts)

    