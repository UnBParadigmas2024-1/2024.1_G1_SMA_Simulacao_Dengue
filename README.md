# 2024.1 Grupo 1 SMA Simulação de Dengue

**Disciplina**: FGA0210 - PARADIGMAS DE PROGRAMAÇÃO - T01 <br>
**Nro do Grupo (de acordo com a Planilha de Divisão dos Grupos)**: 01<br>
**Paradigma**: SMA<br>

## Alunos

|Matrícula | Aluno |
| -- | -- |
| 19/0023376 |   Abraão Alves Ribeiro |
| 19/0103302 |   Bernardo Chaves Pissutti |
| 19/0026600 |   Davi Marinho da Silva Campos | 
| 17/0161871 |   Denniel William Roriz Lima| 
| 19/0105267 |   Diógenes Dantas Lélis Júnior| 
| 18/0113321 |   Francisco Mizael Santos da Silva | 
| 23/2022952 |   Leonardo de Souza Takehana| 
| 19/0091720 |   Lucas Macedo Barboza |
| 19/0093196 |   Mateus Caltabiano Neves Frauzino| 
| 19/0094257 |   Paulo Henrique Rezende |
| 19/0047968 |   Paulo Vitor Silva Abi Acl 

## Sobre

O projeto visa demonstrar a propagação da dengue de maneira visual e utilizando o paradigma de Sistemas Multiagente (SMA). 

## Screenshots

Adicione 2 ou mais screenshots do projeto em termos de interface e/ou funcionamento.

## Instalação

**Linguagens**: Python<br>
**Tecnologias**: Docker<br>

<!-- Descreva os pré-requisitos para rodar o seu projeto e os comandos necessários.
Insira um manual ou um script para auxiliar ainda mais.
Gifs animados e outras ilustrações são bem-vindos! -->

1. Instalar o Docker em https://docs.docker.com/get-docker/
2. Instalar o Docker compose em seu ambiente

### Linux

Para instalação no Linux siga as instruções da página https://docs.docker.com/desktop/install/linux-install/

### MacOS

Para instalação no MacOS siga as instruções da página https://docs.docker.com/desktop/install/mac-install/

### Windows

Para instalação no Windows siga as instruções da página https://docs.docker.com/desktop/install/windows-install/

3. Dê clone do projeto

```
git clone https://github.com/UnBParadigmas2024-1/2024.1_G1_SMA_Simulacao_Dengue/tree/main
```

4. Entre na pasta

```
cd 2024.1_G1_SMA_Simulacao_Dengue
```

5. Inicie o projeto

```
docker-compose up --build
```

Ou

```
docker compose up --build
```

6. Acessar Interface

Abra o navegador e acesse o `http://localhost:8521`

Obs: Para linux é necessário utilizar o comando sudo antes.

Caso as bibliotecas necessárias não tenham sido instaladas ao rodar `docker-compose --build`, pode ser neessário instalá-las separadamente. Para isso, basta rodar em seu terminal o seguinte comando.

```
pip install mesa numpy matplotlib
```

## Uso

Para utilizar o projeto, com a interface aberta no navegador, basta clicar no botão `start` do canto superior direito e a simulação se iniciará. 

O primeiro gráfico mostra o comportamento dos agentes e abaixo dele a quantidade de cada agente. 

Na parte superior ao centro da tela, é possível selecionar quantos frames se passarão a cada segundo, ou seja, é possível alterar a velocidade com que a simulação se passa na tela. 

E por fim, na esquerda, é possível configurar a quantidade inicial de cada agente.

<!-- Explique como usar seu projeto.
Procure ilustrar em passos, com apoio de telas do software, seja com base na interface gráfica, seja com base no terminal.
Nessa seção, deve-se revelar de forma clara sobre o funcionamento do software. -->

### Organização de tarefas

O grupo foi separado em quatro grupos menores para as atividades ficarem melhor organizadas. A divisão de tarefas entre cada subgrupo foi a seguinte:

- **Grupo 1**: Criar o Modelo de Contaminação;
- **Grupo 2**: Criação do Agente Pessoas;
- **Grupo 3** : Criação do Agente Mosquito
- **Grupo 4**: Criação do Objeto Água Parada;

## Vídeo

Adicione 1 ou mais vídeos com a execução do projeto.
Procure:
(i) Introduzir o projeto;
(ii) Mostrar passo a passo o código, explicando-o, e deixando claro o que é de terceiros, e o que é contribuição real da equipe;
(iii) Apresentar particularidades do Paradigma, da Linguagem, e das Tecnologias, e
(iV) Apresentar lições aprendidas, contribuições, pendências, e ideias para trabalhos futuros.
OBS: TODOS DEVEM PARTICIPAR, CONFERINDO PONTOS DE VISTA.
TEMPO: +/- 15min

## Participações

Apresente, brevemente, como cada membro do grupo contribuiu para o projeto.
|Nome do Membro | Contribuição | Significância da Contribuição para o Projeto (Excelente/Boa/Regular/Ruim/Nula) |
| -- | -- | -- |
| Paulo Henrique | |
| Paulo Vitor Silva Abi Acl | | |
| Leonardo de Souza Takehana | |
| Davi Marinho da Silva Campos | | |
| Diógenes Dantas Lélis Júnior | | |
| Bernardo Chaves Pissutti | | |
| Abraão Alves | Ajuda na criação do Agente pessoas | Boa |
| Denniel William Roriz Lima |  ||
| Francisco Mizael Santos da Silva | | |
| Mateus Caltabiano Neves Frauzino |  ||
| Lucas Macedo Barboza | Ajuda na criação do Agente pessoas, ajustes no agente mosquito. | Boa |

## Outros

Quaisquer outras informações sobre o projeto podem ser descritas aqui. Não esqueça, entretanto, de informar sobre:

### Lições aprendidas

### Percepções

### Contribuições e Fragilidades

### Trabalhos Futuros

## Fontes

Referencie, adequadamente, as referências utilizadas.
Indique ainda sobre fontes de leitura complementares.
