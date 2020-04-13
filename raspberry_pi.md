# Raspberry Pi 4 

## INSTALANDO RASPBIAN

1. Fazer o download da imagem do SO (**Raspbian**): https://www.raspberrypi.org/downloads/raspbian/

2. Baixar o programa **Balena Etcher** para subir a ISO no SD Card: https://www.balena.io/etcher/

Feito isso, a Raspberry já está pronta para ser usada! 

## GPIO 

<img src="imagens\GPIO.png" alt="gpio">

Também é possível usar o comando 
        
        pinout



## Configurar WiFi

Créditos: @vitordangelo

Para configurar o wifi na raspberry, crie um arquivo **sem extensão** na raiz  com o nome: 

        wpa_supplicant.conf

Com o código:

        country=BR
        ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
        update_config=1

        network={
                ssid="NETWORK-NAME"
                psk="NETWORK-PASSWORD"
        }

        

## Câmera

Nesta seção, vamos abordar alguns comandos úteis e algumas instruções para usar a câmera da Raspberry Pi.
Para isso, inicialmente, habilite a câmera em *Raspberri Pi Configuration -> Interface - > Camera*.
Em seguida, reinicie a Rasp com o comando

        sudo reboot

Crie um arquivo chamado *camera.py* e insira o código:

        ## Importa a bilbioteca
        from picamera import PiCamera
        from time import sleep

        ## Define um nome para a câmera
        camera = PiCamera()

        camera.start_preview()
        sleep(5)
        camera.stop_preview()

