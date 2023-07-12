# Sistema de Doação de Sangue

Este é um projeto de um sistema de doação de sangue desenvolvido em Python, utilizando o framework CustomTkinter para a interface gráfica e o banco de dados PostgreSQL para armazenar os dados.

## Recursos

- Cadastro de novos doadores
- Registro de bolsas de sangue
- Remoção de doadores

## Pré-requisitos

- Python 3.7 ou superior
- PostgreSQL

## Configuração

1. Clone este repositório:

    git clone https://github.com/seu-usuario/nome-do-repositorio.git

2. Instale as dependências do projeto:

    pip install -r requirements.txt

3. Crie um banco de dados no PostgreSQL chamado "doacaoDeSangue".

4. Execute o script `database.sql` para criar as tabelas necessárias no banco de dados.

5. Abra o arquivo `main.py` e configure as informações de conexão com o banco de dados na seção "Estabelecer a conexão com o banco de dados".

6. Execute o arquivo `main.py` para iniciar o sistema.


## Etapas

Etapa 1: Descrição de Requisitos

Nesta etapa, são descritos os requisitos do sistema de doação de sangue. Isso envolve identificar as funcionalidades, os dados necessários, os usuários envolvidos e quaisquer restrições ou regras específicas.
Etapa 2: Modelagem do diagrama ER

Nesta etapa, é feita a modelagem do diagrama Entidade-Relacionamento (ER). O diagrama ER é uma representação gráfica das entidades do sistema, seus relacionamentos e os atributos associados a cada entidade.
Etapa 3: Mapeamento do Modelo Relacional

Nesta etapa, o diagrama ER é mapeado para um modelo relacional, que consiste na criação de tabelas, definição de chaves primárias e estrangeiras, e estabelecimento de relacionamentos entre as tabelas.
Etapa 4: Normalização

Nesta etapa, é realizada a normalização do modelo relacional. A normalização é o processo de organização das tabelas e eliminação de redundâncias, garantindo que o banco de dados esteja estruturado de forma eficiente.
Etapa 5: SGBD (Esquema, consultas e Visão)

Nesta etapa, são definidos o esquema do banco de dados, as consultas que serão realizadas e as visões necessárias. O esquema descreve a estrutura e as relações do banco de dados, enquanto as consultas e visões são utilizadas para recuperar informações específicas.
Etapa 6: Função, gatilho e usuários

Nesta etapa, são definidas funções, gatilhos e usuários adicionais, caso necessário. As funções são blocos de código que podem ser chamados para executar tarefas específicas, os gatilhos são acionados automaticamente em resposta a eventos no banco de dados, e os usuários são criados para controlar o acesso e permissões no sistema.
Etapa 7: Aplicação

Nesta etapa, a aplicação propriamente dita é desenvolvida, utilizando a modelagem e estrutura definidas nas etapas anteriores. Isso envolve a implementação das funcionalidades do sistema de doação de sangue, como cadastro de doadores, agendamento de doações, entre outras.

