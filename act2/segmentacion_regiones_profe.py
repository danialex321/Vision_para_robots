# Programa para segmentar regiones de interés en función del color
import cv2
import numpy as np

if __name__ == '__main__':
    print("Inicio")
    # Abrimos la imagen
    img = cv2.imread("im1.jpeg")
    print(img.shape)

    # Cambiamos de tamaño (opcional)
    f = 0.5
    img_resized = cv2.resize(img, (0,0), fx=f, fy=f)

    # Tomamos una muestra de la región de interés
    x_ini = 560
    y_ini = 760
    s_ini = 10
    sample = img_resized[int(y_ini*f):int(y_ini*f + s_ini), int(x_ini*f):int(x_ini*f + s_ini), :] # x=560, y=760
    #print(sample)
    min_sample = np.min(sample, axis=(0,1))
    max_sample = np.max(sample, axis=(0,1))
    
    print("minimo: ", min_sample)
    print("maximo: ", max_sample)

    # Umbralizamos
    img_bin = cv2.inRange(img_resized, min_sample, max_sample)

    # Limpiamos ruido en la imagen
    kernel = np.ones((5,5), np.uint8)
    img_closed = cv2.morphologyEx(img_bin, cv2.MORPH_CLOSE, kernel)

    # Buscamos contornos
    contours, hier = cv2.findContours(img_closed, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    print(contours)
    #print(hier)

    # Dibujamos contornos
    img_cnts = cv2.drawContours(img_resized, contours, -1, (0,0,255), 2)

    # Guardamos resultado
    #cv2.imshow("img", img)
    cv2.imshow("img_resized", img_resized)
    cv2.imshow("img_bin", img_bin)
    cv2.imshow("img_closed", img_closed)
    cv2.imshow("contours", img_cnts)
    cv2.waitKey(0)

    # Guardamos resultado
    cv2.imwrite("resultado.png", img_cnts)

    