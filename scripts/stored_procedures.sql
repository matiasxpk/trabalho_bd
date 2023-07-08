/*Antes de criar o STORED PROCEDURED "RealizarDoacao" adicione a coluna "total_doacoes" à tabela "doador" 
--os campos dessa coluna atualiza sempre que uma bolsa de sangue é registrada utilizando o stored procedure "RealizarDoacao" */
ALTER TABLE doador
ADD COLUMN total_doacoes INTEGER DEFAULT 0;

/*Se quiser atualizar o valor do campo "total_doações" com os dados já existentes na tabela "bolsa_de_sangue" 
antes de ser usado o STORED PROCEDURED "RealizarDoacao", execute a seguinte instrução:*/
UPDATE doador
SET total_doacoes = (
    SELECT COUNT(*) 
    FROM bolsa_de_sangue 
    WHERE bolsa_de_sangue.cpf = doador.cpf
);


--Registrar uma bolsa de sangue na "bolsa_de_sangue" e atualizar o total de doações do doador na tabela "Doador"
CREATE OR REPLACE PROCEDURE RealizarDoacao( --recebe quatro parâmetros
    IN p_codigo_bolsa_sangue INT,
    IN p_cpf VARCHAR(11),
    IN p_data DATE,
    IN p_cnpj VARCHAR(14)
)
LANGUAGE plpgsql
AS $$

BEGIN
    INSERT INTO bolsa_de_sangue (codigo, cpf, data, cnpj) --insere uma nova linha na tabela "bolsa_de_sangue"
    VALUES (p_codigo_bolsa_sangue, p_cpf, p_data, p_cnpj);

    UPDATE Doador 
    SET total_doacoes = total_doacoes + 1 --atualiza a tabela "DOADOR", incrementando o valor do campo "total_doações" em 1
    WHERE CPF = p_cpf;                    --onde o CPF do doador seja igual ao parâmetro "p_cpf"

    RAISE NOTICE 'Doação registrada com sucesso.'; --exibe uma mensagem que a doação foi registrada com sucesso
END;
$$

--Exemplo de como pode ser chamado o procedimento
CALL RealizarDoacao(11, '56789012345', '2023-05-07', '21981639000175');


