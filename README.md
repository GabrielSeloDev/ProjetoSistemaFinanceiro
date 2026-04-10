# Sistema de Gestão Financeira

# Descrição do Sistema

Este projeto é uma aplicação web desenvolvida em Python com Flask, projetada para facilitar o controle de finanças pessoais de forma intuitiva, organizada e segura.
O sistema permite que os usuários gerenciem suas contas, estruturem categorias de gastos e registrem todas as suas entradas e saídas financeiras, garantindo um acompanhamento preciso do seu orçamento.
A aplicação foi construída utilizando o ecossistema do Flask (através de Blueprints e Templates HTML). O foco principal é fornecer uma interface de usuário fluida para o controle de caixa, garantindo a segurança dos dados usando os relacionamentos de banco de dados e regras de negócio definidas no back-end.


# Explicação das Tabelas (Banco de Dados)

O sistema utiliza um banco de dados relacional (SQLite), estruturado com a biblioteca SQLAlchemy. Abaixo estão as tabelas principais e suas funções:

tb_usuario : Armazena os dados dos clientes do sistema. 
    Campos principais: id, nome, email (único).

tb_conta : Representa as contas bancárias ou carteiras do usuário. Relaciona-se diretamente com o usuário criador.
    Campos principais: id, nome, usuario_id (Chave Estrangeira).

tb_categoria : Usada para classificar os lançamentos (ex: Alimentação, Salário, Lazer). 
    Campos principais: id, nome, cor (para identificação visual), usuario_id (Chave Estrangeira).

tb_lancamento : A tabela central do sistema. Registra as movimentações financeiras.
    Campos principais: id, nome, data (gerada automaticamente pelo banco), tipo (Enum: entrada/saída), valor, e as chaves estrangeiras (usuario_id, conta_id, categoria_id).


# Lista de Rotas

O sistema foi organizado utilizando Flask Blueprints. Abaixo estão as principais rotas implementadas:

 Módulo de Usuários  
 GET /usuarios/ : Renderiza a tela com a lista de todos os usuários cadastrados.  
 GET /usuarios/novo : Renderiza o formulário HTML para criação de um novo usuário.  
 POST /usuarios/novo : Recebe os dados do formulário e salva o novo usuário no banco.  
 POST /usuarios/<id>/deletar : Remove um usuário específico pelo ID e redireciona a   tela.

Módulo de Lançamentos  
GET /lancamentos/novo : Renderiza o formulário de registro de nova movimentação   financeira.
POST /lancamentos/novo : Aplica as regras de negócio e cadastra o lançamento no banco   de dados.

Módulo de Páginas     
GET / : Renderiza a página principal do sistema.  
GET /sobre : Renderiza a página com informações sobre o sistema.  

Módulo de Categorias  
GET /categorias/ : Renderiza a tela com a lista de todas as categorias cadastradas, ordenadas por usuário.  
GET /categorias/novo : Renderiza o formulário HTML para a criação de uma nova categoria.  
POST /categorias/novo : Recebe os dados do formulário e salva a nova categoria no banco de dados.  
POST /categorias/deletar/<id> : Remove uma categoria específica pelo ID e redireciona para a lista atualizada.  

Módulo de Contas  
GET /contas/ : Renderiza a tela com a lista de todas as contas cadastradas.  
GET /contas/novo : Renderiza o formulário HTML para a criação de uma nova conta.  
POST /contas/novo : Recebe os dados do formulário e salva a nova conta no banco de dados.  
GET /contas/<id>/editar : Renderiza o formulário HTML preenchido com os dados de uma conta específica para edição.  
POST /contas/<id>/editar : Recebe os novos dados e atualiza as informações da conta no banco de dados.  
POST /contas/deletar/<id> : Remove uma conta específica pelo ID e redireciona para a lista atualizada.  


# Regras de Negócio

Para garantir a confiabilidade e a lógica do controle financeiro, as seguintes regras de negócio foram implementadas diretamente no back-end:

1.  Bloqueio de Valores Negativos: O sistema não permite a inserção de valores matematicamente negativos em um lançamento financeiro. A distinção entre receita e despesa é feita exclusivamente pelo tipo da operação.
2.  Tipagem Restrita: Um lançamento só pode ser classificado estritamente como `entrada` ou `saida`. Qualquer outro valor tentado será rejeitado pelo sistema e pelo banco de dados.
3.  Automação de Datas: A data e a hora do lançamento não dependem da digitação do usuário, sendo registradas automaticamente pelo servidor  no momento exato da transação.
