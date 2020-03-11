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
# Introdução a orientação a objetos

## Criação de classes

Em java, podemos criar uma classe da seguinte forma:

    public class Conta {
        int numero; 
        String donoDaConta;
        float saldo;
        float limite;

    }
    
Utilizando o método de criação de classes, o código abaixo se refere a Aula 02 do curso. 

### Arquivo Aula02.java

    /*
     * To change this license header, choose License Headers in Project Properties.
     * To change this template file, choose Tools | Templates
     * and open the template in the editor.
     */
    package aula02;

    /**
     *
     * @author aluno
     */
    public class Aula02 {

        /**
         * @param args the command line arguments
         */
        public static void main(String[] args) {
            Conta conta = new Conta();
            conta.numero = 1234;
            conta.donoDaConta = "Matheus";
            conta.saldo = 1000;
            conta.limite = 100;

            System.out.println("Conta");
            System.out.println("Número: " + conta.numero);
            System.out.println("Dono: " + conta.donoDaConta);
            System.out.println("Saldo: " + conta.saldo);
            System.out.println("Limite: " + conta.limite);

            conta.deposita(500);
            System.out.println("Saldo após depósito: " + conta.saldo);

            if (!conta.saca(50)) {
                System.out.println("Não foi possível realizar o saque");

            } else {
                System.out.println("Saldo após saque: " + conta.saldo);

            }
        }

    }


### Arquivo Conta.java

    /*
     * To change this license header, choose License Headers in Project Properties.
     * To change this template file, choose Tools | Templates
     * and open the template in the editor.
     */
    package aula02;

    /**
     *
     * @author aluno
     */
    public class Conta {

        int numero;
        String donoDaConta;
        float saldo;
        float limite;

        boolean saca(float quantia) {

            if (saldo > quantia) {
                saldo = saldo - quantia;
                return true;

            } else {
                return false;
            }

        }

        void deposita(float quantia) {
            float novoSaldo = saldo + quantia;
            saldo = novoSaldo;
        }

    }

### Exercício 1


/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package exercicio1;

/**
 *
 * @author aluno
 */
public class Exercicio1 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        AnimalPet pet1 = new AnimalPet();
        AnimalPet pet2 = new AnimalPet();
        AnimalPet pet3 = new AnimalPet();

        pet1.comida = "ração";
        pet1.nome = "bob";
        pet1.especie = "cachorro";
        pet1.idade = 5;
        pet1.som = "au au";

        pet2.comida = "carne";
        pet2.nome = "sherek";
        pet2.especie = "ogro";
        pet2.idade = 96;
        pet2.som = "DYOAGDAKHS";

        pet3.comida = "carniça";
        pet3.nome = "desconhecido";
        pet3.especie = "estranho demais pra saber";
        pet3.idade = 789453;
        pet3.som = "kjdsk";

        pet1.mostraInfos();
        pet1.comer();
        pet1.dormir(5);

        pet2.mostraInfos();

        pet3.mostraInfos();

    }

}
/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package exercicio1;

/**
 *
 * @author aluno
 */
public class AnimalPet {

    String nome;
    String especie;
    String som;
    String comida;
    int idade;

    void comer() {
        System.out.println("Hora de comer");
    }

    void dormir(int horas) {
        System.out.println("Hora de dormir " + horas + " horas");
    }

    void movimentar(int metros) {
        System.out.println("Hora de se movimentar " + metros + " metros");
    }

    void fazerBarulho() {
        System.out.println("Hora de fazer barulho!");
    }

    void mostraInfos() {
        System.out.println("Informações do animal:");
        System.out.println("Nome: " + nome);
        System.out.println("Idade: " + idade);
        System.out.println("Som: " + som);
        System.out.println("Comida: " + comida);
    }
}

### Exercício 3

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package exercicio2;

/**
 *
 * @author aluno
 */
public class Exercicio2 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
  
        Trabalhador t1 = new Trabalhador();
        Trabalhador t2 = new Trabalhador();
        Trabalhador t3 = new Trabalhador();
        
        t1.nome = "Matheus";
        t1.profissao = "Engenheiro";
        t1.salario = 15000;
        t1.rg = "MG123456";
        t1.dataNascimento = "05/01/1998";
        
        t2.nome = "Tiago";
        t2.profissao = "Médico";
        t2.salario = 20000;
        t2.rg = "MG4212413";
        t2.dataNascimento = "30/06/1975";
        
        t3.nome = "Maria Eduarda";
        t3.profissao = "Arquiteta";
        t3.salario = 6000;
        t3.rg = "MG8445";
        t3.dataNascimento = "07/10/2000";
        
        t1.calculaGanhoAnual();
        
        t2.mostrarInfosFuncionario();
        
        t3.recebeAumento(2000);
    }
    
}



/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package exercicio2;

/**
 *
 * @author aluno
 */
public class Trabalhador {
    String nome;
    String profissao;
    float salario;
    String rg;
    String dataNascimento;
    
    
    void recebeAumento(float aumento){
    
        salario = salario + aumento;
        System.out.println(salario);
    }
    
    void calculaGanhoAnual(){
        float anual;
        anual = salario*12;
    System.out.println("Ganho anual de: R$ " + anual );
    }
    
    void mostrarInfosFuncionario(){
    System.out.println("Informações do funcionário:");
        System.out.println("Nome: " + nome);
        System.out.println("Profissão: " + profissao);
        System.out.println("Salário: " + salario);
        System.out.println("RG: " + rg);
        System.out.println("Data de Nasciemento: " + dataNascimento);
    }
}



    
