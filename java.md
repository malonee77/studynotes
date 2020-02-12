# Introdução ao JAVA

Utilizaremos o J2SE (Java 2 Standard Edition) e a IDE NetBeans para desenvolvimento. 

### Hello Word 

O comando abaixo, printa uma mensagem. 

    System.out.println("Hello Java");
    System.out.println("Olá turma");
    
O segundo comando não pula linha. 

Outra opção é usar o \n para pular linhas também. Exemplo:

        System.out.println("Hello Java \n");
     
### Atalhos 

Para montar as estruturas de decisão e repetição, ao digitar, apertar TAB imediatamente. Por exemplo, *for + TAB*.

Para identar o código, o atalho é Alt + Shift + f. 

### Comentário

O comentário é feito por //, por exemplo:

    // Essa linha é um comentário. 
    /* Esse comentário pode ter mais de uma linha. */
   
### Variáveis e Tipos primitivos 

Essa linguagem, exige que ao declarar uma variável, declare-se o seu tipo. 

        boolean, byte, short, int, long, float, double e char

Para armazenar um texto deve-se declarar uma variável tipo *string*

        String msg="INATEL";
        System.out.println(msg.length()); // Exibe o comprimento da String
        System.out.println(msg.toUpperCase()); // Transforma em caixa alta
        System.out.println(msg.equalsIgnoreCase(outra_string)); // Compara duas strings
        // Entre outras 
        
### Exemplo de média entre variáveis

        int ano1 = 560, ano2 = 670, ano3 = 540;
        float media = (ano1 + ano2 + ano3) / 3;
        System.out.print("A média de vilões apreendidos é: ");
        System.out.println(media);
        System.out.print("A soma é: ");
        System.out.println(media * 3);

        
