# Programa para segmentar regiones de interés en función del color
import cv2
import numpy as np

if __name__ == '__main__':
    print("Inicio")
    # Abrimos la imagen
    img = cv2.imread("im2.jpeg");

    # Cambiamos de tamaño (opcional)
    f=0.5
    img_resized=cv2.resize(img, (0,0), fx=f, fy=f)

    kernel = np.array([[1/9, 1/9, 1/9],
                      [1/9, 1/9, 1/9],
                      [1/9, 1/9, 1/9]])
    img_filtered = cv2.filter2D(img_resized, -1, kernel)
    # Guardamos resultado
    #cv2.imshow("img",img)
    cv2.imshow("img_resized", img_resized)
    cv2.imshow("img_filtered", img_filtered)

    cv2.waitKey(0)
