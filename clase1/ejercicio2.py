import cv2

if __name__ == '__main__':
    #leer la imagen
    img = cv2.imread("img2.jpg")

    #cambiar el espacio de color de una imagen
    img2 = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    img3 = cv2.cvtColor(img, cv2.COLOR_BGR2Lab)
    
    #visualizar imagenes
    cv2.imshow("RGB", img)
    cv2.imshow("HSV", img2)
    #show ONLY ONE CHANNEL
    cv2.imshow("H", img2[:,:,0])
    cv2.imshow("S", img2[:,:,1])
    cv2.imshow("V", img2[:,:,2])
    cv2.waitKey(0)

    cv2.imshow("L", img3[:,:,0])
    cv2.imshow("a", img3[:,:,1])
    cv2.imshow("b", img3[:,:,2])
    cv2.waitKey(0)
    
