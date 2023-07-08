--CRIANDO USUÁRIOS COM PERMISSÕES ESPECÍFICAS PARA O BANCO DE DADOS "doacaoDeSangue"
--Antes de executar os comandos, certifique-se de que o banco de dados "doacaDeSangue" esteja criado

CREATE USER marcos WITH PASSWORD '123_adm'; --criando usuário marcos com senha 123_adm
GRANT ALL PRIVILEGES ON DATABASE doacaoDeSangue TO marcos; --concede todos as permissões para o banco de dados "doacaoDeSangue" / para isso você tem que ter o banco de dados "doacaoDeSangue" criado


CREATE USER carla WITH PASSWORD '123_leitura'; --criando usuário carla com senha 123_leitura
GRANT CONNECT ON DATABASE doacaoDeSangue TO carla; --concede o acesso de se conectar ao banco de dados "doacaoDeSangue"
GRANT USAGE ON SCHEMA public TO carla;             --usar o esquema público 
GRANT SELECT ON ALL TABLES IN SCHEMA public TO carla; --e fazer consultas de select em todas as tabelas do esquema


