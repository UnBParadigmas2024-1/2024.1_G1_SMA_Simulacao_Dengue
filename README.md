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

O projeto visa demonstrar a propagação da dengue de maneira visual e utilizando o paradigma de Sistemas Multiagente (SMA). A simulação se inicia com uma quantidade pré-definidade de cada agente (Mosquito, Pessoa e Água parada), que pode ser configurada da maneira que o usuário desejar, entre 1 e 20 de cada agente. Na simulação, os agentes interagem entre si, sendo que os mosquitos podem infectar água parada e pessoas, as pessoas podem remover água parada e água infectada gera mais mosquitos.

## Uso do MESA

Este projeto utiliza o framework MESA para a modelagem baseada em agentes. O MESA é um framework robusto e flexível, permitindo a criação de simulações complexas de maneira estruturada e eficiente. Sua documentação completa está disponível [aqui](https://mesa.readthedocs.io/en/stable/).


## Screenshots

![Screenshot 1](./img/layout.png)

Página Inicial do Projeto

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
- **Grupo 3**: Criação do Agente Mosquito
- **Grupo 4**: Criação do Objeto Água Parada;

## Vídeo

[Assista ao Vídeo](https://unbbr-my.sharepoint.com/:v:/g/personal/190026600_aluno_unb_br/ETuj2ymfw0RImjgIFtBUj5oBlgHocDlpwdoGv33N0uQ7SA?e=ZFP1Dz&nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJTdHJlYW1XZWJBcHAiLCJyZWZlcnJhbFZpZXciOiJTaGFyZURpYWxvZy1MaW5rIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXcifX0%3D)

## Adição de Agentes

```Python

class DengueContaminationModel(Model):
    def __init__(self, width, height, initial_people, initial_mosquitoes, initial_water):
        # Inicializa as variáveis do modelo
        self.initial_people = initial_people
        self.initial_mosquitoes = initial_mosquitoes
        self.initial_water = initial_water

        # Define a grade do modelo e o agendador
        self.grid = MultiGrid(width, height, True)
        self.schedule = RandomActivation(self)

        # Contadores de agentes
        self.num_people = initial_people
        self.num_mosquitoes = initial_mosquitoes

        # Inicializa o DataCollector para capturar dados durante a simulação
        self.datacollector = DataCollector(
            model_reporters={
                "Total People": lambda m: self.get_person_count(),
                "Total Mosquitoes": lambda m: self.get_mosquito_count(),
            },
            agent_reporters={
                "State": lambda a: getattr(a, "state", None), 
                "Infections": lambda a: getattr(a, "infections", 0)
            }
        )

        # **Criação e inserção dos agentes na simulação**
        # Cria e insere agentes Pessoa
        for _ in range(self.initial_people):
            pessoa = PersonAgent(uuid.uuid1(), self)
            self.place_agent_randomly(pessoa)  # Posiciona o agente de forma aleatória na grade

        # Cria e insere agentes Mosquito
        for _ in range(self.initial_mosquitoes):
            mosquito = MosquitoAgent(uuid.uuid1(), self)
            self.place_agent_randomly(mosquito)  # Posiciona o agente de forma aleatória na grade
        
        # Cria e insere objetos de Água Parada
        for _ in range(self.initial_water):
            water = WaterObject(uuid.uuid1(), self)
            self.place_agent_randomly(water)  # Posiciona o agente de forma aleatória na grade

    def place_agent_randomly(self, agent):
        """Posiciona um agente de forma aleatória em uma célula vazia da grade"""
        x = self.random.randrange(self.grid.width)
        y = self.random.randrange(self.grid.height)
        if self.grid.is_cell_empty((x, y)):
            self.grid.place_agent(agent, (x, y))  # Posiciona o agente na grade
            self.schedule.add(agent)  # Adiciona o agente ao agendador

    # Outros métodos do modelo...
```

## Participações

Apresente, brevemente, como cada membro do grupo contribuiu para o projeto.
|Nome do Membro | Contribuição | Significância da Contribuição para o Projeto (Excelente/Boa/Regular/Ruim/Nula) |
| -- | -- | -- |
| Abraão Alves | Ajuda na criação do Agente pessoas | Boa |
| Bernardo Chaves Pissutti | Ajudei a desenvolver o agente da água e as interações desse agente com os agentes do mosquito e da pessoa e a mostrar a evolução  da quantidade de mosquitos na simulação. | Boa |
| Davi Marinho da Silva Campos |  Ajudei na criação da ideia do projeto e das regras necessárias, também criei o código inicial dos agentes, a estrutura do projeto e o layout, e posteriormente ajudei nos agentes mosquito e pessoa e na finalização do projeto.  | Boa |
| Denniel William Roriz Lima | Estrutura do projeto, resolução de bugs e ajustes funções de step, movimentação, ajustes nas funções de PersonAgent, WaterObject e MosquitoAgent. Significância da Contribuição para o Projeto | Excelente |
| Diógenes Dantas Lélis Júnior | Ajuda na criação do Modelo de Contaminação e ajustes no agente pessoa | Boa |
| Francisco Mizael Santos da Silva | | |
| Leonardo de Souza Takehana | Correção e edição de alguns bugs e melhoria do modelo, como a adição de probabilidades de progressão da doença, reprodução dos mosquitos e também criação de novas poças | Boa | 
| Lucas Macedo Barboza | Ajuda na criação do Agente pessoas, ajustes no agente mosquito. | Boa |
| Mateus Caltabiano Neves Frauzino | Correção na atualização do gráfico e elaboração da função que conta pessoas, partipação na elaboração do readme | Boa |
| Paulo Henrique | Participei do desenvolvimento do agente mosquito, mais especificamente na interação do mosquito com a pessoa. Criei o método responsável por picar pessoa, caso exista uma pessoa na mesma célula que o mosquito o mesmo pica/infecta a pessoa e checa se a pessoa está infectada para transmitir o vírus para o mosquito. | Boa |
| Paulo Vitor Silva Abi Acl | | |


## Outros

### Lições aprendidas
Durante o desenvolvimento deste projeto, aprendemos sobre a complexidade do paradigma SMA e como ele pode ser aplicado para modelar interações realistas entre agentes autônomos. Também percebemos a importância da colaboração e divisão de tarefas para gerenciar o tempo e entregar um projeto de qualidade.

### Percepções
O uso de MESA para modelagem baseada em agentes foi uma experiência enriquecedora, proporcionando uma nova perspectiva sobre simulações computacionais e como elas podem ser usadas para entender fenômenos do mundo real, como a propagação de doenças.

### Contribuições e Fragilidades
As contribuições foram significativas, especialmente na criação de modelos realistas para a propagação da dengue. No entanto, identificamos fragilidades no equilíbrio entre a complexidade da simulação e a clareza dos resultados apresentados. Futuras iterações podem focar em aprimorar essas áreas.

### Trabalhos Futuros
Para trabalhos futuros, consideramos a implementação de diferentes cenários de propagação, como variáveis climáticas que afetem a população de mosquitos e a inclusão de agentes de saúde pública que possam intervir na simulação. Além disso, melhorias na visualização e no desempenho da simulação são objetivos para versões subsequentes do projeto.

## Fontes

https://github.com/UnBParadigmas2023-1-Turma02/2023.1_G2_SMA_SimuladorDoenca
https://github.com/UnBParadigmas2023-2/2023.2_G4_SMA
https://www.gov.br/saude/pt-br/assuntos/saude-de-a-a-z/a/arboviroses/informe-semanal/informe-semanal-no-02-coe

Esse projeto se diferencia por incrementar a água parada que consegue ser tanto contaminada como também gerar mais mosquitos de forma probabilistica, ele possui diferenciação quando pica uma pessoa infectada ou não colocando chances da pessoa se curar e tempo de vida. Ele também corre por mais de um step ou seja a velocidade é maior que um humano também no modelo de simulação
