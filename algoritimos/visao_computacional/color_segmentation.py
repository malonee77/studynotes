import cv2
import numpy as np
 
imgRGB = cv2.imread("cubo_magico.jpg")
imgHSV = cv2.cvtColor(imgRGB, cv2.COLOR_BGR2HSV)

red_low = np.array([160, 100, 100])
red_high = np.array([200, 255, 255])

yellow_low = np.array([10,100,100])
yellow_high = np.array([50,255,255])

green_low = np.array([40, 100, 100])
green_high = np.array ([80, 255, 255])



mask_red = cv2.inRange(imgHSV, red_low, red_high)
mask_yellow = cv2.inRange(imgHSV, yellow_low, yellow_high)
mask_green = cv2.inRange(imgHSV, green_low, green_high)

imgSegmentada = cv2.Canny(mask_yellow, 100, 200)

red = cv2.bitwise_and(imgRGB, imgRGB, mask = mask_red)
yellow = cv2.bitwise_and(imgRGB, imgRGB, mask = mask_yellow)
green = cv2.bitwise_and(imgRGB, imgRGB, mask = mask_green)



# cv2.imshow("Vermelho", red)
cv2.imshow("Amarelo", yellow)
# cv2.imshow("Verde", green)
cv2.imshow("Cubo Magico", imgRGB)
cv2.imshow("Segmentada", imgSegmentada) # apenas o contorno da imagem amarela

cv2.waitKey(0)
cv2.destroyAllWindows()
