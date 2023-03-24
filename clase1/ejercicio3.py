import cv2

if __name__ == '__main__':
    #leer la imagen
    img = cv2.imread("img3.jpg")

    #cambiar el espacio de color de una imagen
    img2 = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    for i in range (img2[:,:,0].shape[0]):
        for j in range (img2[:,:,0].shape[1]):
            if img2[i,j,0] > 0 and img2[i,j,0] < 20:
                img2[i,j,0] = 255
            else:
                img2[i,j,0] = 0 
    
#visualizar imagen umbralizada
cv2.imshow("imagen original", img)
cv2.imshow("imagen umbralizada", img2[:,:,0])
cv2.waitKey(0)
