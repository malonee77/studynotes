# Análise por visão computacional

Referência: Introdução a Visão Computacional de Felipe Barelli

Os códigos são desenvolvidos em Python usando a biblioteca OpenCV.
## Introdução

O processo de análise de imagens por visão computacional ocorre seguindo um mesmo fluxograma de etapas. São elas:

1. Aquisição de Imagem
2. Pré-Processamento
3. Segmentação
4. Extração de Características
5. Reconhecimento de Padrões
6. Resultado

## Importando uma imagem através de um arquivo

    import cv2

    imagem = cv2.imread("imagem.jpg")
    cv2.imshow("Imagem", imagem)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

## Capturando uma imagem através de um vídeo

    import cv2

    captura = cv2.VideoCapture("video.mp4")

    while True:
      ret, frame = captura.read()
      cv2.imshow("Imagem", frame)

      if cv2.waitKey(1) & 0xFF == ord("q"):
        break

    captura.release()
    cv2.destroyAllWindows()
    
## Capturando uma imagem a partir de uma câmera (webcam)

    import cv2

    captura = cv2.VideoCapture(0)

    while True:
      ret, frame = captura.read()
      cv2.imshow("Imagem", frame)

      if cv2.waitKey(1) & 0xFF == ord("q"):
        break

    captura.release()
    cv2.destroyAllWindows()
