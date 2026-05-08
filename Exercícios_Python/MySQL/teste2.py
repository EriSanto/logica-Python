import mysql.connector
from mysql.connector import Error



def criar_banco(conexao, nome):
    cursor = conexao.cursor()
    #cursor.execute(f"DROP DATABASE {nome};")
    #cursor.execute(f"CREATE DATABASE {nome};")
    cursor.execute(f"USE {nome}")
    
    #cursor.execute("CREATE TABLE fornecedores(codigo int(4) AUTO_INCREMENT, nome varchar(30) NOT NULL, email varchar(50), PRIMARY KEY (codigo));")
   # conexao.commit()
    


def mondificar_fornecedor(conexao):
    cursor = conexao.cursor()
    
    cursor.execute("UPDATE fornecedores SET emprego='Logista' WHERE codigo=6;")
    conexao.commit()

def delet_fornecedor(conexao, codigo):
    cursor = conexao.cursor()
    # Exemplo de consulta
    # cursor.execute("INSERT INTO fornecedores(codigo, nome, email) VALUES (null, 'Leticia', 'leticia@gmail.com')")
    # conexao.commit()
    #cursor.execute(f"DELETE FROM fornecedores WHERE codigo={codigo};")
   # conexao.commit()


def criar_fornecedor(conexao):
    cursor = conexao.cursor()
    
    cursor.execute("INSERT INTO fornecedores(codigo, nome, email) VALUES (null, 'Leticia', 'leticia@gmail.com')")
    conexao.commit()

def inicio():
    conexao = None
    print("inicio")
    try:
        # Configurações de conexão
        # Configurações de conexão
        conexao = mysql.connector.connect(
            host='localhost',
            user='eriky',
            password='senha',
            database='bancobrasil',
            use_pure=True
    )
        
        if conexao.is_connected():
            print("Conectado ao MySQL com sucesso!")
            cursor = conexao.cursor()
            
            #criar_fornecedor(conexao)
            mondificar_fornecedor(conexao)
            
            #criar_banco(conexao, "BancoBrasil")
            
                
            
    except Exception as e:
        print("Teste");
        print(f"Erro ao conectar: {e}")
        
    finally:
        print("Teste");
        if conexao and conexao.is_connected():
            cursor.close()
            conexao.close()
            print("Conexão MySQL encerrada.")

if __name__ == "__main__":
    inicio()