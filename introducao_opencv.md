# Introdução ao OpenCV 

Caso tenha dificuldades em instalar o opencv, veja o passo a passo aqui:

// colocar link do repositorio

## Importando e exibindo uma imagem
  
  import cv2
  import numpy as np 
  
  input = cv2.read('home/pi/Downloads/f1.jpg')
  cv2.imshow('F1 Car', input)
  cv2.waitKey()
  cv2.destroyAllWindows()
    
