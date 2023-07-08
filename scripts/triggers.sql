--TRIGGERS

--atualizar a coluna "data" de uma tabela com a data atual antes de realizar uma inserção
CREATE OR REPLACE FUNCTION registrar_data()
RETURNS TRIGGER 
LANGUAGE plpgsql
AS $$
BEGIN
    NEW.data := current_date; --atribuir data atual à coluna "data" do novo registro que vai ser inserido
    RETURN NEW;
END;
$$;
--atualiza automaticamente a coluna "data" da tabela "bolsa_de_sangue" com a data atual antes de inserir uma nova linha
CREATE TRIGGER registrar_data_bolsa_trigger
BEFORE INSERT ON bolsa_de_sangue --acionado antes da inserção ocorrer na tabela "bolsa_de_sangue"
FOR EACH ROW
EXECUTE FUNCTION registrar_data(); --função será executada quando o gatilho for acionado 
