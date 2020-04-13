# Teclado e Mouse via Smartphone

O aplicativo que vamos usar é o Unfield Remote, ele permite substituir o teclado e o mouse da raspberry pelo smartphone. 

Para isso, devemos seguir os seguintes passos:

Abra o terminal e dê o seguinte comando:

        $ wget -O urserver.deb http://www.unifiedremote.com/d/<rpi-deb>

Caso haja algum erro de SSL, trocar o *http://www.* por *http://http.*. 

Instale os pacotes usando:

        sudo dpkg -i urserver.deb

A instalação seguirá o seguinte diretório:

        /opt/urserver/

Logs serão armazenados em 

        ~/.urserver/


Inicie o Server com: 

         ./opt/urserver/urserver-start


Para fechar op Server, use:

        
     ./opt/urserver/urserver-stop


Para desinstalar a aplicação:

     sudo dpkg -r urserver



Além disso, garanta que o App esteja instalado em seu smartphone. 