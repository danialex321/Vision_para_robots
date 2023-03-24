# Programa para detectar orillas en las imágenes
import cv2
import numpy as np

if __name__ == '__main__':
    print("inicio")
    # Abrimos la imagen
    img = cv2.imread("im1.jpeg")

    # Cambiamos espacio de color
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Cambiamos de tamaño (opcional)
    f = 0.5
    img_resized = cv2.resize(img_gray, (0,0), fx=f, fy=f)

    # Aplicar la operación de filtrado (convolución 2D)
    
    # Filtro promedio
    #kernel = np.array([[1/9,1/9,1/9],
    #                   [1/9,1/9,1/9],
    #                   [1/9,1/9,1/9]])

    # Filtro promedio
    kernel = 1/49*np.ones((7,7))
    img_resized = cv2.filter2D(img_resized, -1, kernel)

    # Filtro gradiente
    kernel1 = np.array([[-1,0,1],
                       [-1,0,1],
                       [-1,0,1]])
    
    kernel2 = np.array([[1,0,-1],
                       [1,0,-1],
                       [1,0,-1]])
    
    kernel3 = np.array([[-1,-1,-1],
                       [0,0,0],
                       [1,1,1]])
    
    kernel4 = np.array([[1,1,1],
                       [0,0,0],
                       [-1,-1,-1]])


    img_filtered1 = cv2.filter2D(img_resized, -1, kernel1)
    img_filtered2 = cv2.filter2D(img_resized, -1, kernel2)
    img_filtered3 = cv2.filter2D(img_resized, -1, kernel3)
    img_filtered4 = cv2.filter2D(img_resized, -1, kernel4)

    # Binarizamos las imagenes
    ret, img_bin1 = cv2.threshold(img_filtered1, 50, 255, cv2.THRESH_BINARY)
    ret, img_bin2 = cv2.threshold(img_filtered2, 50, 255, cv2.THRESH_BINARY)
    ret, img_bin3 = cv2.threshold(img_filtered3, 50, 255, cv2.THRESH_BINARY)
    ret, img_bin4 = cv2.threshold(img_filtered4, 50, 255, cv2.THRESH_BINARY)

    # Resultado total
    img_filtered = img_bin1 + img_bin2 + img_bin3 + img_bin4

    # Filtramos
    #kernel = np.ones((3,3), np.uint8)
    #img_filtered = cv2.erode(img_filtered, kernel, iterations=1)

    cv2.imshow("img", img_resized)
    cv2.imshow("img_final", img_filtered)
    cv2.imshow("img_bin", img_bin1)
    cv2.imshow("img_filtered", img_filtered1)
    cv2.waitKey(0)
