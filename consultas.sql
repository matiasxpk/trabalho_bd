--função agregada e group by
--retorna o número total de doadores para cada tipo sanguíneo presente na tabela DOADOR
SELECT tipo_sanguineo, COUNT(*) as total_doadores --resultado renomeado como "total_doadores"
FROM doador
GROUP BY tipo_sanguineo; --registro serão de acordo com o "tipo_sanguineo"


--consulta aninhada
--retorna nomes dos hospitais que têm registro na tabela "recebe"
SELECT nome
FROM hospital
WHERE cnpj IN (SELECT cnpj_hospital FROM recebe); --retorna os valores da coluna "cnpj_hospital" da tabela RECEBE


--INNER JOIN
--retorna os campos "cpf", "nome", "email" da tabela DOADOR e o "numero" da tabela TELEFONE_DOADOR que possuem CPF em ambas as tabelas
SELECT d.cpf, d.nome, d.email, t.numero
FROM doador d
INNER JOIN telefone_doador t ON d.cpf = t.cpf; --cpf na tabela DOADOR seja igual ao CPF na tabela TELEFONE_DOADOR


--OUTER JOIN
--retorna os campos "nome" da tabela DOADOR e o "numero " da tabela "TELEFONE_DOADOR". Com LEFT JOIN todos os registros da tabela DOADOR são retornados, independentemente se tiver telefones correspondentes na tabela "TELEFONE_DOADOR"
SELECT d.nome, t.numero
FROM doador d
LEFT JOIN telefone_doador t ON d.cpf = t.cpf; 


--GROUP BY e HAVING
--retorna os valores da coluna cnpj_hospital que aparecem na tabela RECEBE mais de uma vez ou pelo menos uma vez
SELECT cnpj_hospital
FROM recebe
GROUP BY cnpj_hospital
HAVING COUNT(*) >= 1; --cpfs com contagem maior ou igual a 1 na tabela "cnpj_hospital" 


--EXISTS
--retorna todos os registro da tabela HOSPITAL que tambem possui pelo menos um registro na tabela TELEFONE_HOSPITAL
SELECT *
FROM hospital h
WHERE EXISTS (SELECT 1 FROM telefone_hospital th WHERE h.cnpj = th.cnpj_hospital);


--ALL
--retorna todos os registros da tabela DOADOR que tem idade maior do que todas as idades dos doadores de tipo sanguineo O+
SELECT nome
FROM doador
WHERE idade > ALL (SELECT idade FROM doador WHERE tipo_sanguineo = 'O+');


--visão
-- retorna cpf e nome do DOADOR, a data de RECEBE e o nome do HOSPITAL que recebeu
CREATE VIEW view_doador_recebimento AS
SELECT d.cpf, d.nome, r.data, h.nome AS nome_hospital
FROM doador d
INNER JOIN bolsa_de_sangue b ON d.cpf = b.cpf
INNER JOIN recebe r ON b.codigo = r.codigo_bolsa
INNER JOIN hospital h ON r.cnpj_hospital = h.cnpj;

SELECT * FROM view_doador_recebimento;
