import psycopg2
import tkinter as tk

# Estabelecer a conexão com o banco de dados
conn = psycopg2.connect(
    host="localhost",
    database="doacaoDeSangue",
    user="postgres",
    password="2612"
)

cur = conn.cursor()


class TelaInicial:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1280x720")
        self.root.configure(bg="white")
        self.root.title("Escolha")

        # Configurar peso das linhas e colunas
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        self.label = tk.Label(root, text="Escolha uma opção:", width=20)
        self.label.grid(row=0, column=0, pady=20)

        self.button_doador = tk.Button(root, text="Doador", command=self.abrir_tela_doador, width=15)
        self.button_doador.grid(row=1, column=0, pady=10)

        self.button_bolsa = tk.Button(root, text="Bolsa de Sangue", command=self.abrir_tela_bolsa, width=15)
        self.button_bolsa.grid(row=2, column=0, pady=10)

    def abrir_tela_doador(self):
        self.root.destroy()  # Fechar a tela inicial
        root = tk.Tk()
        TelaDoador(root)
        root.mainloop()

    def abrir_tela_bolsa(self):
        self.root.destroy()  # Fechar a tela inicial
        root = tk.Tk()
        TelaBolsaSangue(root)
        root.mainloop()

class TelaDoador:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1280x720")
        self.root.configure(bg="white")
        self.root.title("Hematocare - Doador")

        # Configurar peso das linhas e colunas
        for i in range(12):
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(2):
            self.root.grid_columnconfigure(i, weight=1)

        self.result_label = tk.Label(root, text="")
        self.result_label.grid(row=0, column=0, columnspan=2, sticky="nsew")

       

        self.label1 = tk.Label(root, text="Digite o CPF:")
        self.label1.grid(row=1, column=0, sticky="e")
        self.entry1 = tk.Entry(root)
        self.entry1.grid(row=1, column=1, padx=10)

        self.label2 = tk.Label(root, text="Digite o nome:")
        self.label2.grid(row=2, column=0, sticky="e")
        self.entry2 = tk.Entry(root)
        self.entry2.grid(row=2, column=1, padx=10)

        self.label3 = tk.Label(root, text="Digite a idade:")
        self.label3.grid(row=3, column=0, sticky="e")
        self.entry3 = tk.Entry(root)
        self.entry3.grid(row=3, column=1, padx=10)

        self.label4 = tk.Label(root, text="Digite o E-mail:")
        self.label4.grid(row=4, column=0, sticky="e")
        self.entry4 = tk.Entry(root)
        self.entry4.grid(row=4, column=1, padx=10)


        self.label5 = tk.Label(root, text="Digite o logradouro:")
        self.label5.grid(row=5, column=0, sticky="e")
        self.entry5 = tk.Entry(root)
        self.entry5.grid(row=5, column=1, padx=10)

        self.label6 = tk.Label(root, text="Digite o número:")
        self.label6.grid(row=6, column=0, sticky="e")
        self.entry6 = tk.Entry(root)
        self.entry6.grid(row=6, column=1, padx=10)

        self.label7 = tk.Label(root, text="Digite o bairro:")
        self.label7.grid(row=7, column=0, sticky="e")
        self.entry7 = tk.Entry(root)
        self.entry7.grid(row=7, column=1, padx=10)

        self.label8 = tk.Label(root, text="Digite a cidade:")
        self.label8.grid(row=8, column=0, sticky="e")
        self.entry8 = tk.Entry(root)
        self.entry8.grid(row=8, column=1, padx=10)

        self.label9 = tk.Label(root, text="Digite o CEP:")
        self.label9.grid(row=9, column=0, sticky="e")
        self.entry9 = tk.Entry(root)
        self.entry9.grid(row=9, column=1, padx=10)

        self.label10 = tk.Label(root, text="Digite o tipo sanguineo:")
        self.label10.grid(row=10, column=0, sticky="e")
        self.entry10 = tk.Entry(root)
        self.entry10.grid(row=10, column=1, padx=10)

        self.label11 = tk.Label(root, text="Digite o telefone:")
        self.label11.grid(row=11, column=0, sticky="e")
        self.entry11 = tk.Entry(root)
        self.entry11.grid(row=11, column=1, padx=10)

        

        self.button1 = tk.Button(root, text="Registrar Novo Doador", command=self.register_doador)
        self.button1.grid(row=12, column=0, columnspan=2)



        """self.button2 = tk.Button(root, text="Registrar Hospital", command=self.register_hospital)
        self.button2.grid(row=12, column=0, columnspan=2)

        self.button3 = tk.Button(root, text="Registrar Funcionário", command=self.register_funcionario)
        self.button3.grid(row=13, column=0, columnspan=2)"""

        self.button4 = tk.Button(root, text="Remover Doador", command=self.remove_doador)
        self.button4.grid(row=13, column=0, columnspan=2)

        self.button5 = tk.Button(root, text="Consultar Doador", command=self.consultar_doador)
        self.button5.grid(row=14, column=0, columnspan=2)



    def register_doador(self):
        cpf = self.entry1.get()
        nome = self.entry2.get()
        idade = self.entry3.get()
        email = self.entry4.get()
        logradouro = self.entry5.get()
        numero = self.entry6.get()
        bairro = self.entry7.get()
        cidade = self.entry8.get()
        cep = self.entry9.get()
        tipo_sanguineo = self.entry10.get()
        telefone = self.entry13.get()

        # Executar instrução SQL para inserir os dados no banco de dados
        cur.execute("INSERT INTO doador (cpf, nome, idade, email, logradouro, numero, bairro, cidade, cep, tipo_sanguineo) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    (cpf, nome, idade, email, logradouro, numero, bairro, cidade, cep, tipo_sanguineo))
        cur.execute("INSERT INTO telefone_doador (cpf, numero) VALUES (%s, %s)",
                    (cpf, numero))
        conn.commit()

        print("CPF:", cpf)
        print("Nome:", nome)
        print("Idade:", idade)
        print("E-mail:", email)
        print("Logradouro:", logradouro)
        print("Número:", numero)
        print("Bairro:", bairro)
        print("Cidade:", cidade)
        print("CEP:", cep)
        print("Tipo Sanguíneo:", tipo_sanguineo)


    def remove_doador(self):
        cpf = self.entry12.get()

        try:
            cur = conn.cursor()

            # Obter os códigos da bolsa de sangue associados ao CPF do doador
            cur.execute("SELECT codigo FROM bolsa_de_sangue WHERE cpf = %s", (cpf,))
            codigos_bolsa = cur.fetchall()


            for codigo in codigos_bolsa:
                cur.execute("DELETE FROM recebe WHERE codigo_bolsa = %s", (codigo,))



            # Excluir os registros das outras tabelas
            cur.execute("DELETE FROM bolsa_de_sangue WHERE cpf = %s", (cpf,))

            cur.execute("DELETE FROM telefone_doador WHERE cpf = %s", (cpf,))
            cur.execute("DELETE FROM atende WHERE cpf = %s", (cpf,))
            cur.execute("DELETE FROM doador WHERE cpf = %s", (cpf,))

            # Confirmar a transação
            conn.commit()

            print(f"Doador com CPF {cpf} removido com sucesso.")
        except Exception as e:
            # Reverter a transação em caso de erro
            conn.rollback()
            print(f"Erro ao remover o doador: {str(e)}")
        finally:
            # Fechar o cursor
            cur.close()


    def register_hospital(self):
        print("Registrar Hospital")

    def register_funcionario(self):
        print("Registrar Funcionário")

    def consultar_doador(self):
        cpf = self.entry1.get()

        # Executar instrução SQL para consultar o doador no banco de dados
        cur.execute("SELECT * FROM doador WHERE cpf = %s", (cpf,))
        results = cur.fetchall()

        if len(results) > 0:
            doador_info = ""
            for row in results:
                doador_info += f"CPF: {row[0]}\nNome: {row[1]}\nIdade: {row[2]}\nE-mail: {row[3]}\n" \
                               f"Logradouro: {row[4]}\nNúmero: {row[5]}\nBairro: {row[6]}\nCidade: {row[7]}\n" \
                               f"CEP: {row[8]}\nTipo Sanguíneo: {row[9]}"
            self.result_label.config(text=doador_info)
            print(doador_info)  # Exibir no terminal
        else:
            self.result_label.config(text="Doador não encontrado")
            print("Doador não encontrado")  # Exibir no terminal

class TelaBolsaSangue:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1280x720")
        self.root.configure(bg="white")
        self.root.title("Hematocare - Bolsa de Sangue")

        # Configurar peso das linhas e colunas
        for i in range(12):
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(2):
            self.root.grid_columnconfigure(i, weight=1)

        self.result_label = tk.Label(root, text="")
        self.result_label.grid(row=0, column=0, columnspan=2, sticky="nsew")

        self.label11 = tk.Label(root, text="Digite o código da bolsa de sangue:")
        self.label11.grid(row=1, column=0, sticky="e")
        self.entry11 = tk.Entry(root)
        self.entry11.grid(row=1, column=1, padx=10)

        self.label11 = tk.Label(root, text="Digite o cpf:")
        self.label11.grid(row=2, column=0, sticky="e")
        self.entry11 = tk.Entry(root)
        self.entry11.grid(row=2, column=1, padx=10)

        self.label11 = tk.Label(root, text="Digite a data:")
        self.label11.grid(row=3, column=0, sticky="e")
        self.entry11 = tk.Entry(root)
        self.entry11.grid(row=3, column=1, padx=10)

        self.label11 = tk.Label(root, text="Digite o CNPJ:")
        self.label11.grid(row=4, column=0, sticky="e")
        self.entry11 = tk.Entry(root)
        self.entry11.grid(row=4, column=1, padx=10)

        self.button1 = tk.Button(root, text="Registrar Bolsa de Sangue", command=self.register_bolsa_de_sangue)
        self.button1.grid(row=5, column=0, columnspan=2)



        """self.button2 = tk.Button(root, text="Registrar Hospital", command=self.register_hospital)
        self.button2.grid(row=12, column=0, columnspan=2)

        self.button3 = tk.Button(root, text="Registrar Funcionário", command=self.register_funcionario)
        self.button3.grid(row=13, column=0, columnspan=2)"""

    def register_bolsa_de_sangue(self):
        codigo = self.entry1.get()
        cpf = self.entry2.get()
        data = self.entry3.get()
        cnpj = self.entry4.get()

        # Executar instrução SQL para inserir os dados no banco de dados
        cur.execute("INSERT INTO bolsa_de_sangue (codigo, cpf, data, cnpj) VALUES (%s, %s, %s, %s)",
                    (codigo, cpf, data, cnpj))
        conn.commit()

        print("Código:", codigo)
        print("CPF:", cpf)
        print("Data:", data)
        print("CNPJ:", cnpj)



root = tk.Tk()
TelaInicial(root)
root.mainloop()

cur.close()