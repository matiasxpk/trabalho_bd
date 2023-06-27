--função agregada e group by
SELECT tipo_sanguineo, COUNT(*) as total_doadores
FROM doador
GROUP BY tipo_sanguineo;

--consulta aninhada
SELECT nome
FROM hospital
WHERE cnpj IN (SELECT cnpj_hospital FROM recebe);

--INNER JOIN
SELECT d.cpf, d.nome, d.email, t.numero
FROM doador d
INNER JOIN telefone_doador t ON d.cpf = t.cpf;

--OUTER JOIN
SELECT d.nome, t.numero
FROM doador d
LEFT JOIN telefone_doador t ON d.cpf = t.cpf;

--GROUP BY e HAVING
SELECT cnpj_hospital
FROM recebe
GROUP BY cnpj_hospital
HAVING COUNT(*) < 5;

--EXISTS
SELECT *
FROM hospital h
WHERE EXISTS (SELECT 1 FROM telefone_hospital th WHERE h.cnpj = th.cnpj_hospital);

--ALL
SELECT nome
FROM doador
WHERE idade > ALL (SELECT idade FROM doador WHERE tipo_sanguineo = 'O+');


--visão
CREATE VIEW view_doador_recebimento AS
SELECT d.cpf, d.nome, r.data, h.nome AS nome_hospital
FROM doador d
INNER JOIN bolsa_de_sangue b ON d.cpf = b.cpf
INNER JOIN recebe r ON b.codigo = r.codigo_bolsa
INNER JOIN hospital h ON r.cnpj_hospital = h.cnpj;


