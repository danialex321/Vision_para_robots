import cv2

if __name__ == '__main__':
    #leer la imagen
    img = cv2.imread("babyapa.jpg")
    #tipo de la imagen
    print(type(img))
    #forma de la imagen
    print(img.shape)
    #acceso a un pixel
    print(img[0,0,0])
    #modificar pixeles
    img[250,250,2] = 0
    #[250,250,:] = (0,255,0)
    #img[250,250,:] = 255
    img[90:100,80:100,:] = (0,255,255)
    #visualizar imagenes
    #cv2.imshow("imagen", img)
    #show ONLY ONE CHANNEL
    cv2.imshow("R", img[:,:,2])
    cv2.imshow("G", img[:,:,1])
    cv2.imshow("B", img[:,:,0])
    cv2.waitKey(0)
    #save image
    cv2.imwrite("prueba.png",img)

