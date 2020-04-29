# Análise por visão computacional, primeiros passos

Referência: Introdução a Visão Computacional de Felipe Barelli

Os códigos são desenvolvidos em Python usando a biblioteca OpenCV.

## Instalação da biblioteca OpenCV no Windows

Para instalar a bilbioteca, abra o terminal do Windows (ctrl+R 'cmd') e digite o comando

	pip install opencv-pyhton

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
   
   
   
## Segmentação por cor

| Cor      | Limite inferior | Limite superior |
| -------- | --------------- | --------------- |
| Amarelo  | 10, 1001 100    | 50, 255, 255    |
| Azul     | 100, 100, 100   | 140, 255, 255   |
| Verde    | 40, 100, 100    | 80, 255, 255    |
| Vermelho | 160, 100, 100   | 200, 255, 255   |


