# Introdução ao OpenCV 

Caso tenha dificuldades em instalar o opencv, veja o passo a passo aqui:

https://github.com/malonee77/raspberrypi/blob/master/opencv.md

## Importando e exibindo uma imagem
  
    import cv2
    import numpy as np 

    input = cv2.read('home/pi/Downloads/f1.jpg')
    cv2.imshow('F1 Car', input)
    cv2.waitKey()
    cv2.destroyAllWindows()

