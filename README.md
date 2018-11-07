# Projeto Estrela da Morte - Reconhecimento de Linguagem Natural e Aplicação IoT

## Introdução

O propósito desse projeto foi integrar o Raspberry Pi 3 com um dashboard online - Ubidots - utilizando o protocolo HTTP, junto com 2 sensores e 2 atuadores à escolha dos integrantes do grupo e o laboratório FabLab. Além disso, decidiu-se integrar serviços da IBM IoT, a fim de garantir inteligência e facilidade no desenvolvimento do sistema. Foi escolhido então desenvolver um modelo da conhecida Estrela da Morte da série de filmes Star Wars.

## Material Utilizado

* Raspberry Pi 3;
* SD Card (16 GB+) - Raspbian OS + Scripts + Node-red;
* Impressora 3D (material PLA ou ABS);
* Sensor de Temperatura DHT11;
* Acelerômetro e Giroscópio MPU6050;
* Buzzer;
* LED;
* 1x Resistor 330 Ω;
* 10 parafusos M3 x 15 mm.

## Princípio Básico de Funcionamento

O modelo possui uma funcionalidade integrada com o IBM Watson, capaz de reconhecer comandos enviados via o aplicativo de mensagens Telegram; seja por texto ou até por voz (tratado pelos serviços TTS e STT da IBM). Isso inclui acender/apagar/piscar o LED, "atirar" com a Estrela da Morte, reproduzir sons pré-definidos, detectar movimento e acionar um alarme e medir a temperatura interna da espaçonave. Todos esses comandos geram uma resposta do sistema confirmando a ação escolhida, reproduzida via conector de áudio do Raspberry Pi.

#### Disparo da Estrela da Morte

O comando via texto ou mensagem de voz pelo Telegram de disparar ativa uma sequência de efeitos divididos em 3 etapas de som e luz com o propósito de simular a funcionalidade da arma.

#### Reprodução de sons e alarme

O modelo também é capaz de executar e reproduzir músicas pré-definidas. Desta forma o sistema, após ter reconhecido e interpretado a linguagem natural, executa scripts Python que alteram a frequência PWM do buzzer, de forma a reproduzir a melodia escolhida. Como exemplo de  músicas, o sistema pode tocar a clássica Marcha Imperial, a música-tema do jogo Mario Brothers et al. Com isso, para solicitar a reprodução da Marcha Imperial, basta ordenar:

```
Tocar música: Marcha Imperial
```

Ainda nesse quesito, é possível acionar um sistema de alarme via dashboard Ubidots que identifica a movimentação do modelo via giroscópio e reage tocando um som semelhante a de um alarme por 5 segundos, enquanto estiver acionado.


#### Temperatura

O sensor de temperatura alimenta continuamente o gráfico do dashboard com até 2 horas de histórico de medições e representações em linha das suas alterações.

## Características do Modelo 3D

A impressão do modelo pode ser feita utilizando os materiais PLA (maior perfeccionismo nos detalhes) ou ABS (maior resistência e durabilidade).

O modelo foi projeto para embarcar um Raspberry Pi 3 com a opção de ventoinha de 30 mm posicionada no topo da cúpula.

A impressão é dividida em 4 partes. São necessários 10 parafusos M3 x 15 mm, sendo que as cúpulas superior e inferior podem ser coladas, se assim o desejar.

O suporte é sólido, e não só é projetado para evitar que a nave role, mas também para não desalinhar o modelo em seu eixo simétrico.

## Detalhes de Programação e Serviços da IBM Utilizados

