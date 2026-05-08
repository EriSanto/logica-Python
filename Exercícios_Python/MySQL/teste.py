import mysql.connector
from mysql.connector import Error


def conectarBanco():
    # Configurações de conexão
    conexao = mysql.connector.connect(
        host='localhost',
        user='eriky',
        password='senha',
        database='bancodeteste',
        use_pure=True
    )
    return conexao

def buscar_fornecedor(id):
    
    conexao = None
    print("inicio")
    try:
        # Configurações de conexão
        conexao = conectarBanco()
        
        if conexao.is_connected():
            print("Conectado ao MySQL com sucesso!")
            cursor = conexao.cursor()
            
            # Exemplo de consulta
            cursor.execute("SELECT * FROM fornecedores where codigo = %s;", [id])
            
            fornecedores = cursor.fetchone()
            
            return fornecedores
        
            
    except Exception as e:
        print("Teste");
        print(f"Erro ao conectar: {e}")
        
    finally:
        print("Teste");
        if conexao and conexao.is_connected():
            cursor.close()
            conexao.close()
            print("Conexão MySQL encerrada.")
      
def inserir_fornecedor(nome, email):
    conexao = None
    print("inicio")
    try:
        # Configurações de conexão
        conexao = conectarBanco()
        
        if conexao.is_connected():
            print("Conectado ao MySQL com sucesso!")
            cursor = conexao.cursor()
            pessoa = [nome, email]
            result = cursor.execute("INSERT INTO fornecedores(codigo, nome, email) VALUES (null, %s, %s);", pessoa)
            conexao.commit()
            print(result)
            
    except Exception as e:
        print("Teste");
        print(f"Erro ao conectar: {e}")
        
    finally:
        print("Teste");
        if conexao and conexao.is_connected():
            cursor.close()
            conexao.close()
            print("Conexão MySQL encerrada.")
    
def pegar_fornecedores():
    conexao = None
    print("inicio")
    try:
        # Configurações de conexão
        conexao = conectarBanco()
        
        if conexao.is_connected():
            print("Conectado ao MySQL com sucesso!")
            cursor = conexao.cursor()
            
            # Exemplo de consulta
            cursor.execute("SELECT * FROM fornecedores;")
            
            fornecedores = cursor.fetchall()
            
            return fornecedores
        
            
    except Exception as e:
        print("Teste");
        print(f"Erro ao conectar: {e}")
        
    finally:
        print("Teste");
        if conexao and conexao.is_connected():
            cursor.close()
            conexao.close()
            print("Conexão MySQL encerrada.")
    
def inicio():
    #inserir_fornecedor("Edipo","edipo@yahoo.com.br")
    #fornecedores = pegar_fornecedores()
    #print(fornecedores[0][1])
    
    
    #inserir_fornecedor("Maria", "maria@gmail.com.br")
    
    fornecedor = buscar_fornecedor(8)
    print(fornecedor)

if __name__ == "__main__":
    inicio()