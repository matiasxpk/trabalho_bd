import psycopg2
import tkinter as tk
import customtkinter
from CTkMessagebox import CTkMessagebox


# Estabelecer a conexão com o banco de dados
conn = psycopg2.connect(
    host="localhost",
    database="doacaoDeSangue",
    user="postgres",
    password="2612"
)

cur = conn.cursor()
text_escolher_opcao = "Escolha uma opção:"
fonte = "Century Gothic bold"

class TelaInicial:
    def __init__(self, root):
        self.root = root
        customtkinter.set_appearance_mode("Dark")
        self.root.geometry("700x400")
        self.root.title("Sistem de Doação de Sangue")
        #self.root.iconbitmap()
        self.root.resizable(False, False)

        self.title = customtkinter.CTkLabel(root, text="Hematocare", font=(fonte, 24), text_color="#fff")
        self.spam = customtkinter.CTkLabel(root, text=text_escolher_opcao, font=(fonte, 16), text_color="#fff" )
        self.title.pack(padx=0, pady=10)
        self.spam.pack(padx=50, pady=70)

        self.button_doador = customtkinter.CTkButton(root, text="Doador", fg_color="#EE0303", command=self.abrir_tela_doador)
        self.button_doador.pack(padx=10, pady=10)

        self.button_bolsa = customtkinter.CTkButton(root, text="Bolsa de Sangue", fg_color="#EE0303", command=self.abrir_tela_bolsa)
        self.button_bolsa.pack(padx=10, pady=10)


    def abrir_tela_doador(self):
        self.root.destroy()  # Fechar a tela inicial
        root = customtkinter.CTk()
        TelaDoador(root)
        root.mainloop()

    def abrir_tela_bolsa(self):
        self.root.destroy()  # Fechar a tela inicial
        root = customtkinter.CTk()
        TelaBolsaSangue(root)
        root.mainloop()

class TelaDoador:
    def __init__(self, root):
        self.root = root
        customtkinter.set_appearance_mode("System")
        self.root.geometry("700x500")
        self.root.title("Doador")
        self.root.resizable(False, False)




        # Configurar peso das linhas e colunas
        for i in range(12):
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(2):
            self.root.grid_columnconfigure(i, weight=1)

        self.spam = customtkinter.CTkLabel(root, text=text_escolher_opcao, font=(fonte, 16), text_color="#fff" )
        self.spam.pack(padx=50, pady=70)
       
        self.button1 = customtkinter.CTkButton(root, text="Registrar Novo Doador", fg_color="#EE0303", command=self.abrir_tela_doador_register)
        self.button1.pack(padx=10, pady=10)

        self.button4 = customtkinter.CTkButton(root, text="Remover Doador", fg_color="#EE0303", command=self.abrir_tela_doador_remover)
        self.button4.pack(padx=10, pady=10)
        
        self.button5 = customtkinter.CTkButton(root, text="Consultar Doador", fg_color="#EE0303", command=self.abrir_tela_doador_consultar)
        self.button5.pack(padx=10, pady=10) 

        self.button6 = customtkinter.CTkButton(root, text="Alterar Dados Doador",fg_color="#EE0303",command=self.abrir_tela_doador_alterar)
        self.button6.pack(padx=10, pady=10)

        self.button_voltar = customtkinter.CTkButton(root, text="Voltar", fg_color="gray", hover_color="#808080", command=self.voltar_tela_inicial)
        self.button_voltar.pack(padx=10, pady=10)


    def voltar_tela_inicial(self):
        self.root.destroy()  # Fechar a tela atual
        root = customtkinter.CTk()
        TelaInicial(root)
        root.mainloop()

    def abrir_tela_doador_register(self):
        self.root.destroy()  # Fechar a tela inicial
        root = customtkinter.CTk()
        RegisterDoador(root)
        root.mainloop()

    def abrir_tela_doador_remover(self):
        self.root.destroy()  # Fechar a tela inicial
        root = customtkinter.CTk()
        RemoverDoador(root)
        root.mainloop()

    def abrir_tela_doador_consultar(self):
        self.root.destroy()  # Fechar a tela inicial
        root = customtkinter.CTk()
        ConsultarDoador(root)
        root.mainloop()

    def abrir_tela_doador_alterar(self):
        self.root.destroy()  # Fechar a tela inicial
        root = customtkinter.CTk()
        AlterarDoador(root)
        root.mainloop()

digiteOCpf = "Dígite o CPF:"

class RegisterDoador:
    def __init__(self, root):
        self.root = root
        customtkinter.set_appearance_mode("System")
        self.root.geometry("700x500")
        self.root.title("Doador")
        self.root.resizable(False, False)



        # Configurar peso das linhas e colunas
        for i in range(12):
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(2):
            self.root.grid_columnconfigure(i, weight=1)

        
                
        self.label1 = customtkinter.CTkLabel(root, text=digiteOCpf)
        self.label1.grid(row=1, column=0, sticky="e")
        self.entry1 = customtkinter.CTkEntry(root)
        self.entry1.grid(row=1, column=1, padx=10)

        self.label2 = customtkinter.CTkLabel(root, text="Digite o nome:")
        self.label2.grid(row=2, column=0, sticky="e")
        self.entry2 = customtkinter.CTkEntry(root)
        self.entry2.grid(row=2, column=1, padx=10)

        self.label3 = customtkinter.CTkLabel(root, text="Digite a idade:")
        self.label3.grid(row=3, column=0, sticky="e")
        self.entry3 = customtkinter.CTkEntry(root)
        self.entry3.grid(row=3, column=1, padx=10)

        self.label4 = customtkinter.CTkLabel(root, text="Digite o E-mail:")
        self.label4.grid(row=4, column=0, sticky="e")
        self.entry4 = customtkinter.CTkEntry(root)
        self.entry4.grid(row=4, column=1, padx=10)

        self.label5 = customtkinter.CTkLabel(root, text="Digite o logradouro:")
        self.label5.grid(row=5, column=0, sticky="e")
        self.entry5 = customtkinter.CTkEntry(root)
        self.entry5.grid(row=5, column=1, padx=10)

        self.label6 = customtkinter.CTkLabel(root, text="Digite o número:")
        self.label6.grid(row=6, column=0, sticky="e")
        self.entry6 = customtkinter.CTkEntry(root)
        self.entry6.grid(row=6, column=1, padx=10)

        self.label7 = customtkinter.CTkLabel(root, text="Digite o bairro:")
        self.label7.grid(row=7, column=0, sticky="e")
        self.entry7 = customtkinter.CTkEntry(root)
        self.entry7.grid(row=7, column=1, padx=10)

        self.label8 = customtkinter.CTkLabel(root, text="Digite a cidade:")
        self.label8.grid(row=8, column=0, sticky="e")
        self.entry8 = customtkinter.CTkEntry(root)
        self.entry8.grid(row=8, column=1, padx=10)

        self.label9 = customtkinter.CTkLabel(root, text="Digite o CEP:")
        self.label9.grid(row=9, column=0, sticky="e")
        self.entry9 = customtkinter.CTkEntry(root)
        self.entry9.grid(row=9, column=1, padx=10)

        self.label10 = customtkinter.CTkLabel(root, text="Digite o tipo sanguineo:")
        self.label10.grid(row=10, column=0, sticky="e")
        self.entry10 = customtkinter.CTkEntry(root)
        self.entry10.grid(row=10, column=1, padx=10)

        self.label11 = customtkinter.CTkLabel(root, text="Digite o telefone:")
        self.label11.grid(row=11, column=0, sticky="e")
        self.entry11 = customtkinter.CTkEntry(root)
        self.entry11.grid(row=11, column=1, padx=10)

        self.button1 = customtkinter.CTkButton(root, text="Registrar Novo Doador", fg_color="#EE0303", command=self.register_doador)
        self.button1.grid(row=13, column=0, padx=10, pady=10)

        self.button_voltar = customtkinter.CTkButton(root, text="Voltar", fg_color="gray", hover_color="#808080", command=self.voltar_tela_doador)
        self.button_voltar.grid(row=13, column=1, padx=10, pady=10)
        


    def voltar_tela_doador(self):
        self.root.destroy()  # Fechar a tela atual
        root = customtkinter.CTk()
        TelaDoador(root)
        root.mainloop()

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
        telefone = self.entry11.get()

        # Executar instrução SQL para inserir os dados no banco de dados
        cur.execute("INSERT INTO doador (cpf, nome, idade, email, logradouro, numero, bairro, cidade, cep, tipo_sanguineo) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    (cpf, nome, idade, email, logradouro, numero, bairro, cidade, cep, tipo_sanguineo))
        cur.execute("INSERT INTO telefone_doador (cpf, numero) VALUES (%s, %s)",
                    (cpf, telefone))
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
        self.show_checkmark()

    def show_checkmark(self):
        # Show some positive message with the checkmark icon
        CTkMessagebox(title="",message="O doador foi cadastrado com sucesso",icon="check", option_1="OK!")
        CTkMessagebox.show()

class RemoverDoador:
    def __init__(self, root):
        self.root = root
        customtkinter.set_appearance_mode("System")
        self.root.geometry("700x500")
        self.root.title("Doador")
        self.root.resizable(False, False)


        

        # Configurar peso das linhas e colunas
        for i in range(12):
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(2):
            self.root.grid_columnconfigure(i, weight=1)
        
        self.result_label = customtkinter.CTkLabel(root, text="")
        self.result_label.grid(row=0, column=0, columnspan=2, sticky="nsew")
        
        self.label1 = customtkinter.CTkLabel(root, text=digiteOCpf)
        self.label1.grid(row=1, column=0, sticky="e")
        self.entry1 = customtkinter.CTkEntry(root)
        self.entry1.grid(row=1, column=1, padx=10)

        self.button4 = customtkinter.CTkButton(root, text="Remover Doador", fg_color="#EE0303",  command=self.remove_doador)
        self.button4.grid(row=11, column=0, padx=10, pady=(70,30))

        self.button_voltar = customtkinter.CTkButton(root, text="Voltar", fg_color="gray", hover_color="#808080", command=self.voltar_tela_doadro)
        self.button_voltar.grid(row=11, column=1, padx=10, pady=(70,30))

    
    def voltar_tela_doadro(self):
        self.root.destroy()  # Fechar a tela atual
        root = customtkinter.CTk()
        TelaDoador(root)
        root.mainloop()

    def remove_doador(self):


        cpf = self.entry1.get()

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
        self.show_checkmark()

    def show_checkmark(self):
        # Show some positive message with the checkmark icon
        CTkMessagebox(title="",message="O doador foi removido",icon="check", option_1="OK!")
        CTkMessagebox.show()
 

class ConsultarDoador:
    def __init__(self, root):
        self.root = root
        customtkinter.set_appearance_mode("System")
        self.root.geometry("700x500")
        self.root.title("Doador")
        self.root.resizable(False, False)

        
            
        # Configurar peso das linhas e colunas
        for i in range(12):
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(2):
            self.root.grid_columnconfigure(i, weight=1)
        
        self.result_label = customtkinter.CTkLabel(root, text="")
        self.result_label.grid(row=0, column=0, columnspan=2, sticky="nsew")
        
        self.label1 = customtkinter.CTkLabel(root, text=digiteOCpf)
        self.label1.grid(row=1, column=0, sticky="e")
        self.entry1 = customtkinter.CTkEntry(root)
        self.entry1.grid(row=1, column=1, padx=10)

        self.button5 = customtkinter.CTkButton(root, text="Consultar Doador", fg_color="#EE0303", command=self.consultar_doador)
        self.button5.grid(row=11, column=0, padx=10, pady=(70,30))  

        self.button_voltar = customtkinter.CTkButton(root, text="Voltar", fg_color="gray", hover_color="#808080", command=self.voltar_tela_doadro)
        self.button_voltar.grid(row=11, column=1, padx=10, pady=(70,30))

    def voltar_tela_doadro(self):
        self.root.destroy()  # Fechar a tela atual
        root = customtkinter.CTk()
        TelaDoador(root)
        root.mainloop()
    
    def abrir_tela_consulta_doador(self, doador_info, root):

        root_resultado = root
        root_resultado.geometry("700x500")
        root_resultado.title("Resultado da Consulta")

        if doador_info:
            resultado_label = customtkinter.CTkLabel(root_resultado, text=doador_info, font=(fonte, 14))
            resultado_label.pack(padx=50, pady=70)
        else:
            messagebox =CTkMessagebox(title="",message="O doador não foi encontrado",icon="warning", option_1="OK!")
            messagebox.show()
        root_resultado.mainloop()

    def consultar_doador(self):
        cpf = self.entry1.get()

        # Executar instrução SQL para consultar o doador no banco de dados
        cur.execute("SELECT * FROM doador WHERE cpf = %s", (cpf,))
        results = cur.fetchall()

        if len(results) > 0:
            doador_info = ""
            for row in results:
                doador_info += f"CPF: {row[0]}\n\nNome: {row[1]}\n\nIdade: {row[2]}\n\nE-mail: {row[3]}\n\n" \
                               f"Logradouro: {row[4]}\n\nNúmero: {row[5]}\n\nBairro: {row[6]}\n\nCidade: {row[7]}\n\n" \
                               f"CEP: {row[8]}\n\nTipo Sanguíneo: {row[9]}\n\n"
        else:
            doador_info = None

        self.abrir_tela_consulta_doador(doador_info, self.root)
        print(doador_info)  # Exibir no terminal # Exibir no terminal

class AlterarDoador:
    def __init__(self, root):
        self.root = root
        customtkinter.set_appearance_mode("System")
        self.root.geometry("700x500")
        self.root.title("Alterar Doador")
        self.root.resizable(False, False)

        
        # Configurar peso das linhas e colunas
        for i in range(12):
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(2):
            self.root.grid_columnconfigure(i, weight=1)

        self.label1 = customtkinter.CTkLabel(root, text=digiteOCpf)
        self.label1.grid(row=1, column=0, sticky="e")
        self.entry1 = customtkinter.CTkEntry(root)
        self.entry1.grid(row=1, column=1, padx=10)

        self.label2 = customtkinter.CTkLabel(root, text="Digite o nome:")
        self.label2.grid(row=2, column=0, sticky="e")
        self.entry2 = customtkinter.CTkEntry(root)
        self.entry2.grid(row=2, column=1, padx=10)

        self.label3 = customtkinter.CTkLabel(root, text="Digite a idade:")
        self.label3.grid(row=3, column=0, sticky="e")
        self.entry3 = customtkinter.CTkEntry(root)
        self.entry3.grid(row=3, column=1, padx=10)

        self.label4 = customtkinter.CTkLabel(root, text="Digite o E-mail:")
        self.label4.grid(row=4, column=0, sticky="e")
        self.entry4 = customtkinter.CTkEntry(root)
        self.entry4.grid(row=4, column=1, padx=10)

        self.label5 = customtkinter.CTkLabel(root, text="Digite o logradouro:")
        self.label5.grid(row=5, column=0, sticky="e")
        self.entry5 = customtkinter.CTkEntry(root)
        self.entry5.grid(row=5, column=1, padx=10)

        self.label6 = customtkinter.CTkLabel(root, text="Digite o número:")
        self.label6.grid(row=6, column=0, sticky="e")
        self.entry6 = customtkinter.CTkEntry(root)
        self.entry6.grid(row=6, column=1, padx=10)

        self.label7 = customtkinter.CTkLabel(root, text="Digite o bairro:")
        self.label7.grid(row=7, column=0, sticky="e")
        self.entry7 = customtkinter.CTkEntry(root)
        self.entry7.grid(row=7, column=1, padx=10)

        self.label8 = customtkinter.CTkLabel(root, text="Digite a cidade:")
        self.label8.grid(row=8, column=0, sticky="e")
        self.entry8 = customtkinter.CTkEntry(root)
        self.entry8.grid(row=8, column=1, padx=10)

        self.label9 = customtkinter.CTkLabel(root, text="Digite o CEP:")
        self.label9.grid(row=9, column=0, sticky="e")
        self.entry9 = customtkinter.CTkEntry(root)
        self.entry9.grid(row=9, column=1, padx=10)

        self.label10 = customtkinter.CTkLabel(root, text="Digite o tipo sanguineo:")
        self.label10.grid(row=10, column=0, sticky="e")
        self.entry10 = customtkinter.CTkEntry(root)
        self.entry10.grid(row=10, column=1, padx=10)

        self.label11 = customtkinter.CTkLabel(root, text="Digite o telefone:")
        self.label11.grid(row=11, column=0, sticky="e")
        self.entry11 = customtkinter.CTkEntry(root)
        self.entry11.grid(row=11, column=1, padx=10)


        self.button1 = customtkinter.CTkButton(root, text="Alterar dados do Doador", fg_color="#EE0303", command=self.alterar_dados_doador)
        self.button1.grid(row=13, column=0, padx=10, pady=10)
        
        self.button_voltar = customtkinter.CTkButton(root, text="Voltar", fg_color="gray", hover_color="#808080", command=self.voltar_tela_inicial)
        self.button_voltar.grid(row=13, column=1, padx=10, pady=10)
        

    def voltar_tela_inicial(self):
        self.root.destroy()  # Fechar a tela atual
        root = customtkinter.CTk()
        TelaDoador(root)
        root.mainloop()

    def alterar_dados_doador(self):
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
        telefone = self.entry11.get()

        # Executar instrução SQL para inserir os dados no banco de dados
        cur.execute("UPDATE doador SET nome = %s, idade = %s, email = %s, logradouro = %s, numero = %s, bairro = %s, cidade = %s, cep = %s, tipo_sanguineo = %s WHERE cpf = %s",
                    (nome, idade, email, logradouro, numero, bairro, cidade, cep, tipo_sanguineo, cpf))

        cur.execute("UPDATE telefone_doador SET numero = %s WHERE cpf = %s",
                    (telefone, cpf))

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
        self.show_checkmark()

    def show_checkmark(self):
        # Show some positive message with the checkmark icon
        CTkMessagebox(title="",message="O doador foi alterado com sucesso",icon="check", option_1="OK!")
        CTkMessagebox.show()
    
titulo = "Bolsa de Sangue"   
class TelaBolsaSangue:
    def __init__(self, root):
        self.root = root
        customtkinter.set_appearance_mode("System")
        self.root.geometry("700x500")
        self.root.title(titulo)
        self.root.resizable(False, False)



        # Configurar peso das linhas e colunas
        for i in range(12):
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(2):
            self.root.grid_columnconfigure(i, weight=1)

        #self.result_label.grid(row=0, column=0, columnspan=2, sticky="nsew")

        self.spam = customtkinter.CTkLabel(root, text=text_escolher_opcao, font=(fonte, 16), text_color="#fff" )
        self.spam.pack(padx=50, pady=70)
       
        self.button1 = customtkinter.CTkButton(root, text="Registrar Bolsa de Sangue", fg_color="#EE0303", command=self.abrir_tela_bolsa_register)
        self.button1.pack(padx=10, pady=10)

        self.button2 = customtkinter.CTkButton(root, text="Remover Bolsa de Sangue", fg_color="#EE0303", command=self.abrir_tela_bolsa_remove)
        self.button2.pack(padx=10, pady=10)
        
        self.button3 = customtkinter.CTkButton(root, text="Consultar Bolsa de Sangue", fg_color="#EE0303", command=self.abrir_tela_bolsa_consulta)
        self.button3.pack(padx=10, pady=10)


        self.button_voltar = customtkinter.CTkButton(root, text="Voltar", fg_color="gray", hover_color="#808080", command=self.voltar_tela_inicial)
        self.button_voltar.pack(padx=10, pady=10)

    def voltar_tela_inicial(self):
        self.root.destroy()  # Fechar a tela atual
        root = customtkinter.CTk()
        TelaInicial(root)
        root.mainloop()

    def abrir_tela_bolsa_consulta(self):
        self.root.destroy()  # Fechar a tela inicial
        root = customtkinter.CTk()
        ConsultaBolsa(root)
        root.mainloop()

    def abrir_tela_bolsa_register(self):
        self.root.destroy()  # Fechar a tela inicial
        root = customtkinter.CTk()
        RegisterBolsa(root)
        root.mainloop()

    def abrir_tela_bolsa_remove(self):
        self.root.destroy()  # Fechar a tela inicial
        root = customtkinter.CTk()
        RemoverBolsa(root)
        root.mainloop()


 # Exibir no terminal
     
class ConsultaBolsa:

    def __init__(self, root):
        self.root = root
        customtkinter.set_appearance_mode("System")
        self.root.geometry("700x500")
        self.root.title(titulo)
        self.root.resizable(False, False)


        # Configurar peso das linhas e colunas
        for i in range(12):
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(2):
            self.root.grid_columnconfigure(i, weight=1)

        self.result_label = customtkinter.CTkLabel(root, text="")
        self.result_label.grid(row=0, column=0, columnspan=2, sticky="nsew")
 
        self.label12 = customtkinter.CTkLabel(root, text=digiteOCpf)
        self.label12.grid(row=2, column=0, sticky="e")
        self.entry12 = customtkinter.CTkEntry(root)
        self.entry12.grid(row=2, column=1, padx=10)

        self.button3 = customtkinter.CTkButton(root, text="Consultar Bolsa de Sangue", fg_color="#EE0303", command=self.consultar_Bolsa_de_Sangue)
        self.button3.grid(row=11, column=0, padx=10, pady=(70,30))

        self.button_voltar = customtkinter.CTkButton(root, text="Voltar", fg_color="gray", hover_color="#808080", command=self.voltar_tela_inicial)
        self.button_voltar.grid(row=11, column=1, padx=10, pady=(70,30))



    def voltar_tela_inicial(self):
        self.root.destroy()  # Fechar a tela atual
        root = customtkinter.CTk()
        TelaBolsaSangue(root)
        root.mainloop()

    def consultar_Bolsa_de_Sangue(self):
        

        cpf = self.entry12.get()

        # Executar instrução SQL para consultar o doador no banco de dados
        cur.execute("SELECT * FROM bolsa_de_sangue WHERE cpf = %s", (cpf,))
        results = cur.fetchall()

        if len(results) > 0:
            doador_info = ""
            for row in results:
                doador_info += f"Código: {row[0]}\n\nCPF: {row[1]}\n\nData: {row[2]}\n\nCNPJ: {row[3]}\n\n" \
                               
        else:
            doador_info = None

        self.abrir_tela_consulta_bolsa(doador_info)
        print(doador_info)  # Exibir no termina

    def abrir_tela_consulta_bolsa(self, doador_info):

        root_resultado = customtkinter.CTk()
        root_resultado.geometry("700x500")
        root_resultado.title("Resultado da Consulta")

        if doador_info:
            resultado_label = customtkinter.CTkLabel(root_resultado, text=doador_info, font=(fonte, 14))
            resultado_label.pack(padx=50, pady=70)
        else:
            CTkMessagebox(title="",message="Bolsa de sangue não foi encontrado",icon="cancel", option_1="OK!")
            CTkMessagebox.show()
        root_resultado.mainloop()

class RemoverBolsa:
    def __init__(self, root):
        self.root = root
        customtkinter.set_appearance_mode("System")
        self.root.geometry("700x500")
        self.root.title(titulo)
        self.root.resizable(False, False)


        # Configurar peso das linhas e colunas
        for i in range(12):
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(2):
            self.root.grid_columnconfigure(i, weight=1)

        self.result_label = customtkinter.CTkLabel(root, text="")
        self.result_label.grid(row=0, column=0, columnspan=2, sticky="nsew")

        self.label12 = customtkinter.CTkLabel(root, text=digiteOCpf)
        self.label12.grid(row=2, column=0, sticky="e")
        self.entry12 = customtkinter.CTkEntry(root)
        self.entry12.grid(row=2, column=1, padx=10)

        self.button2 = customtkinter.CTkButton(root, text="Remover Bolsa de Sangue", fg_color="#EE0303", command=self.remover_Bolsa_de_Sangue)
        self.button2.grid(row=11, column=0, padx=10, pady=(70,30))

        self.button_voltar = customtkinter.CTkButton(root, text="Voltar", fg_color="gray", hover_color="#808080", command=self.voltar_tela_inicial)
        self.button_voltar.grid(row=11, column=1, padx=10, pady=(70,30))


    def voltar_tela_inicial(self):
        self.root.destroy()  # Fechar a tela atual
        root = customtkinter.CTk()
        TelaBolsaSangue(root)
        root.mainloop()

    def remover_Bolsa_de_Sangue(self):

        cpf = self.entry12.get()

        try:
            cur = conn.cursor()

            # Obter os códigos da bolsa de sangue associados ao CPF do doador
            
            cur.execute("DELETE FROM bolsa_de_sangue WHERE cpf = %s", (cpf,))

            # Confirmar a transação
            conn.commit()

            print(f"Bolsa de sangue do portador do CPF {cpf} removido com sucesso.")
        except Exception as e:
            # Reverter a transação em caso de erro
            conn.rollback()
            print(f"Erro ao remover o doador: {str(e)}")
        finally:
            # Fechar o cursor
            cur.close()
        self.show_checkmark()

    def show_checkmark(self):
    # Show some positive message with the checkmark icon
        CTkMessagebox(title="",message="Bolsa de sangue foi removido",icon="check", option_1="OK!")
        CTkMessagebox.show()
class RegisterBolsa:
    def __init__(self, root):
        self.root = root
        customtkinter.set_appearance_mode("System")
        self.root.geometry("700x500")
        self.root.title(titulo)
        self.root.resizable(False, False)


        # Configurar peso das linhas e colunas
        for i in range(12):
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(2):
            self.root.grid_columnconfigure(i, weight=1)

        self.result_label = customtkinter.CTkLabel(root, text="")
        self.result_label.grid(row=0, column=0, columnspan=2, sticky="nsew")

        self.label11 = customtkinter.CTkLabel(root, text="Digite o código da bolsa de sangue:")
        self.label11.grid(row=1, column=0, sticky="e")
        self.entry11 = customtkinter.CTkEntry(root)
        self.entry11.grid(row=1, column=1, padx=10)

        self.label12 = customtkinter.CTkLabel(root, text=digiteOCpf)
        self.label12.grid(row=2, column=0, sticky="e")
        self.entry12 = customtkinter.CTkEntry(root)
        self.entry12.grid(row=2, column=1, padx=10)

        self.label13 = customtkinter.CTkLabel(root, text="Digite a data:")
        self.label13.grid(row=3, column=0, sticky="e")
        self.entry13 = customtkinter.CTkEntry(root)
        self.entry13.grid(row=3, column=1, padx=10)

        self.label14 = customtkinter.CTkLabel(root, text="Digite o CNPJ:")
        self.label14.grid(row=4, column=0, sticky="e")
        self.entry14 = customtkinter.CTkEntry(root)
        self.entry14.grid(row=4, column=1, padx=10)

        self.button1 = customtkinter.CTkButton(root, text="Registrar Bolsa de Sangue",fg_color="#EE0303", command=self.register_bolsa_de_sangue)
        self.button1.grid(row=11, column=0, padx=10, pady=(70,30))

        self.button_voltar = customtkinter.CTkButton(root, text="Voltar", fg_color="gray", hover_color="#808080", command=self.voltar_tela_inicial)
        self.button_voltar.grid(row=11, column=1, padx=10, pady=(70,30))


    def voltar_tela_inicial(self):
        self.root.destroy()  # Fechar a tela atual
        root = customtkinter.CTk()
        TelaBolsaSangue(root)
        root.mainloop()

    def register_bolsa_de_sangue(self):

        

        codigo = self.entry11.get()
        cpf = self.entry12.get()
        data = self.entry13.get()
        cnpj = self.entry14.get()

        # Executar instrução SQL para inserir os dados no banco de dados
        cur.execute("INSERT INTO bolsa_de_sangue (codigo, cpf, data, cnpj) VALUES (%s, %s, %s, %s)",
                    (codigo, cpf, data, cnpj))
        conn.commit()

        print("Código:", codigo)
        print("CPF:", cpf)
        print("Data:", data)
        print("CNPJ:", cnpj)
        self.show_checkmark()

    def show_checkmark(self):
    # Show some positive message with the checkmark icon
        CTkMessagebox(title="",message="Bolsa de sangue foi cadastrado com sucesso",icon="check", option_1="OK!")
        CTkMessagebox.show()

root = customtkinter.CTk()
TelaInicial(root)
root.mainloop()

cur.close()
