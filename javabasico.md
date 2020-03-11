# Introdução ao JAVA

Utilizaremos o J2SE (Java 2 Standard Edition) e a IDE NetBeans para desenvolvimento. 

Para baixar a IDE, acessar:

> https://netbeans.apache.org/download/index.html

### Hello Word 

O comando abaixo, printa uma mensagem. 

    System.out.println("Hello Java");
    System.out.print("Olá turma");

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
        int soma = ano1 + ano2 + ano3;
        float media = (ano1 + ano2 + ano3) / 3;
        System.out.println("A média de vilões apreendidos é: " + media);
        System.out.println("A soma é: " + soma);

>  Para definir a quantidade de casas decimais, usar: %Xf em que X é o numero de casas decimais.
### Entrada de Dados via terminal 

Para fazer a leitura de dados, devemos usar a função Scanner. 

Devemos importar a biblioteca: 

        import java.util.Scanner;

Veja abaixo um exemplo onde atribuímos valores para os anos 1, 2 e 3. 

        Scanner teclado = new Scanner(System.in);

        System.out.print("Ano 1: ");
        int ano1 = teclado.nextInt();

        System.out.print("Ano 2: ");
        int ano2 = teclado.nextInt();

        System.out.print("Ano 3: ");
        int ano3 = teclado.nextInt();


### IF ELSE

 Um programa básico de cálculo de nota de aprovação no semestre. 

        int NPA, NP3;
        Scanner npa = new Scanner(System.in);
        Scanner np3 = new Scanner(System.in);
        System.out.print("Entre com a NPA: ");
        NPA = npa.nextInt();

        if (NPA >= 60) {

            System.out.print("Aprovado! ");

        } else {
            System.out.println("Vish, pegou NP3 mano! :/ ");
            System.out.print("Entre com a NP3: ");
            NP3 = np3.nextInt();

            if ((NPA + NP3) / 2 >= 50) {

                System.out.print("Aprovado! ");
            } else {

                System.out.print("Reprovado ");
            }

        }
