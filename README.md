# Projeto IoT - Estrela da Morte

## Introdução

O propósito desse projeto foi integrar o Raspberry Pi 3 com um dashboard online - Ubidots - utilizando o protocolo HTTP, junto com 2 sensores e 2 atuadores à escolha dos integrantes do grupo e o laboratório FabLab. Além disso, decidiu-se integrar serviços da IBM IoT, a fim de garantir inteligência e facilidade no desenvolvimento do sistema. Foi escolhido então desenvolver um modelo da conhecida Estrela da Morte da série de filmes Star Wars.

## Material Utilizado

* Raspberry Pi 3;
* Impressora 3D (material PLA ou ABS);
* Sensor de Temperatura DHT11;
* Acelerômetro e Giroscópio MPU6050;
* Buzzer;
* LED.

## Princípio Básico de Funcionamento

O modelo possui uma funcionalidade integrada com o IBM Watson, capaz de reconhecer comandos enviados via o aplicativo de mensagens Telegram; seja por texto ou até por voz (tratamento via serviços Text To Speech e Speech to Text). Isso inclui acender/apagar/piscar o LED, "disparar" a Estrela da Morte, reproduzir sons pré-definidos, detectar movimento e acionar um alarme e medir a temperatura. Todos esses comandos geram uma resposta do sistema confirmando a ação escolhida, reproduzida via conector de áudio do Raspberry Pi.

## Características do Modelo 3D

A impressão do modelo pode ser feita utilizando os materiais PLA (maior perfeccionismo nos detalhes) ou ABS (maior resistência e durabilidade).

O modelo foi projeto para embarcar um Raspberry Pi 3 com a opção de ventoinha de 30mm posicionada no topo da cúpula.

A impressão é dividida em 4 partes. São necessários 10 parafusos M3 x 15mm, sendo que as cúpulas superior e inferior podem ser coladas, se assim o desejar.

O suporte é sólido, e não só é projetado para evitar que a nave role, mas também para não desalinhar o modelo em seu eixo simétrico.

## Detalhes de Programação e Serviços da IBM Utilizados

