from flask import Flask, request, jsonify
import mysql.connector
from mysql.connector import Error
from flask_cors import CORS
from datetime import date
import random

app = Flask(__name__)
CORS(app)

def conexao():
    try:
        con_BD = mysql.connector.connect(
            host='localhost',
            user='root',
            password='40028922',
            database='projeto_bd_site_de_jogos'
        )
        if con_BD.is_connected():
            print("A conexão foi um sucesso!")
            return con_BD
    except Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")
        return None
    


#-----------------------------------------------------------------------------------------------------------------------------
# Códigos Jogo
#-----------------------------------------------------------------------------------------------------------------------------
def inserir_jogo(db, idJogo, Descrição, Titulo, Categoria, Data_Lancamento, Capa, Processador, Memoria_RAM, Placa_de_Vídeo, Armazenamento):
    try:
        cursor = db.cursor()
        
        # Ler o arquivo de imagem em modo binário
        with open(Capa, 'rb') as file:
            Foto_perfil = file.read()
        
        sql = """
        INSERT INTO jogo (idJogo, Descrição, Titulo, Categoria, Data_Lancamento, Capa, Processador, Memoria_RAM, Placa_de_Vídeo, Armazenamento)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        valores = (idJogo, Descrição, Titulo, Categoria, Data_Lancamento, Foto_perfil, Processador, Memoria_RAM, Placa_de_Vídeo, Armazenamento)
        cursor.execute(sql, valores)
        db.commit()
        print("Jogo inserido com sucesso.")
    except Error as e:
        db.rollback()
        print(f"Erro ao inserir jogo: {e}")
    finally:
        cursor.close()

def deletar_jogo(db, idJogo): 
    try:
        cursor = db.cursor()
        sql = """
        DELETE FROM jogo
        WHERE idJogo = %s
        """
        cursor.execute(sql, (idJogo,))
        db.commit()
        print("Jogo deletado com sucesso.")
    except Error as e:
        db.rollback()
        print(f"Erro ao deletar jogo: {e}")
    finally:
        db.close()

#-----------------------------------------------------------------------------------------------------------------------------
# Códigos Biblioteca_de_Jogos
#-----------------------------------------------------------------------------------------------------------------------------

def inserir_biblioteca_jg(db, idBiblioteca_de_Jogos, Status_Instalação, Data_de_Adição):
    try:
        cursor = db.cursor()
        
        sql = """
        INSERT INTO biblioteca_de_jogos (idBiblioteca_de_Jogos, Status_Instalação, Data_de_Adição)
        VALUES (%s, %s, %s)
        """
        valores = (idBiblioteca_de_Jogos, Status_Instalação, Data_de_Adição)
        cursor.execute(sql, valores)
        db.commit()
        print("Biblioteca de jogos feita com sucesso.")
    except Error as e:
        db.rollback()
        print(f"Erro ao fazer a biblioteca de jogos: {e}")
    finally:
        cursor.close()

def deletar_biblioteca_jg(db, idBiblioteca_de_Jogos): 
    try:
        cursor = db.cursor()
        sql = "DELETE FROM biblioteca_de_jogos WHERE idBiblioteca_de_Jogos = %s"
        cursor.execute(sql, (idBiblioteca_de_Jogos,))
        db.commit()
        print("Biblioteca deletada com sucesso.")
    except Error as e:
        db.rollback()
        print(f"Erro ao deletar a biblioteca: {e}")
    finally:
        cursor.close()
#-----------------------------------------------------------------------------------------------------------------------------
# Códigos Perfil_Usuário
#-----------------------------------------------------------------------------------------------------------------------------

def inserir_perfil_usuario(db, idPerfil_Usuário, caminho_foto_perfil, Biografia, Localização):
    try:
        cursor = db.cursor()
        
        Foto_perfil = None
        
        if isinstance(caminho_foto_perfil, str) and caminho_foto_perfil.strip():
            try:
                with open(caminho_foto_perfil, 'rb') as file:
                    Foto_perfil = file.read()
            except (FileNotFoundError, OSError):
                print(f"Arquivo de imagem não encontrado ou erro ao abrir o arquivo: {caminho_foto_perfil}. Inserindo valor None para Foto_perfil.")
        else:
            print("Caminho da foto de perfil inválido ou não fornecido. Inserindo valor None para Foto_perfil.")
        
        sql = """
        INSERT INTO perfil_usuário (idPerfil_Usuário, Foto_perfil, Biografia, Localização)
        VALUES (%s, %s, %s, %s)
        """
        valores = (idPerfil_Usuário, Foto_perfil, Biografia, Localização)
        cursor.execute(sql, valores)
        db.commit()
        print("Perfil do usuário inserido com sucesso.")
    except Error as e:
        db.rollback()
        print(f"Erro ao inserir perfil do usuário: {e}")
    finally:
        cursor.close()

def deletar_perfil_usuario(db, idPerfil_Usuário):
    try:
        cursor = db.cursor()
        sql = "DELETE FROM perfil_usuário WHERE idPerfil_Usuário = %s"
        cursor.execute(sql, (idPerfil_Usuário,))
        db.commit()
        print("Perfil do usuário deletado com sucesso.")
    except Error as e:
        db.rollback()
        print(f"Erro ao deletar perfil do usuário: {e}")
    finally:
        cursor.close()
    
#-----------------------------------------------------------------------------------------------------------------------------
# Códigos Loja
#-----------------------------------------------------------------------------------------------------------------------------

def inserir_loja(db, idLoja, Preço, ID_Jogo):
    try:
        cursor = db.cursor()
        
        sql = """
        INSERT INTO loja (idLoja, Preço, ID_Jogo)
        VALUES (%s, %s, %s)
        """
        valores = (idLoja, Preço, ID_Jogo)
        cursor.execute(sql, valores)
        db.commit()
        print("Loja inserido com sucesso.")
    except Error as e:
        db.rollback()
        print(f"Erro ao inserir loja: {e}")
    finally:
        cursor.close()

def deletar_loja(db, idLoja):
    try:
        cursor = db.cursor()
        
        sql = "DELETE FROM loja WHERE idLoja = %s"
        valores = (idLoja,)
        cursor.execute(sql, valores)
        db.commit()
        print("Loja deletada com sucesso.")
    except Error as e:
        db.rollback()
        print(f"Erro ao deletar loja: {e}")
    finally:
        cursor.close()

#-----------------------------------------------------------------------------------------------------------------------------
# Códigos Carrinho_de_Compras
#-----------------------------------------------------------------------------------------------------------------------------

def inserir_carrinho_compras(db, idCarrinho_de_Compras, Data_de_Adição, Quantidade, ID_Loja):
    try:
        cursor = db.cursor()
        
        id_jogo_random = 77 #random.randint(1,5)
        inserir_loja(db, ID_Loja, 'R$0,00', id_jogo_random)
        
        sql = """
        INSERT INTO carrinho_de_compras (idCarrinho_de_Compras, Data_de_Adição, Quantidade, ID_Loja)
        VALUES (%s, %s, %s, %s)
        """
        valores = (idCarrinho_de_Compras, Data_de_Adição, Quantidade, ID_Loja)
        cursor.execute(sql, valores)
        db.commit()
        print("Carrinho inserido com sucesso.")
    except Error as e:
        db.rollback()
        print(f"Erro ao inserir carrinho: {e}")
    finally:
        cursor.close()

def deletar_carrinho(db, idCarrinho_de_Compras): 
    try:
        cursor = db.cursor()
        
        # Seleciona o ID_Loja do carrinho de compras
        cursor.execute("SELECT ID_Loja FROM carrinho_de_compras WHERE idCarrinho_de_Compras = %s", (idCarrinho_de_Compras,))
        id_loja = cursor.fetchone()[0]
        
        # Deleta a loja correspondente
        deletar_loja(db, id_loja)
        
        # Deleta o carrinho de compras
        sql = "DELETE FROM carrinho_de_compras WHERE idCarrinho_de_Compras = %s"
        cursor.execute(sql, (idCarrinho_de_Compras,))
        db.commit()
        print("Carrinho deletado com sucesso.")
    except Error as e:
        db.rollback()
        print(f"Erro ao deletar o carrinho: {e}")
    finally:
        cursor.close()

#-----------------------------------------------------------------------------------------------------------------------------
# Códigos Usuário
#-----------------------------------------------------------------------------------------------------------------------------

# Rota para adicionar usuário
@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    db = conexao()
    if db:
        try:
            cursor = db.cursor()

            id_biblioteca = random.randint(1, 10000)
            id_perfil_usuario = random.randint(1, 10000)
            id_carrinho_compras = random.randint(1, 10000)
            id_loja_random = random.randint(1, 10000)
            data_cadastro = date.today()
            inserir_biblioteca_jg(db, id_biblioteca, 0, data_cadastro)
            inserir_perfil_usuario(db, id_perfil_usuario, "None", "Biografia", "Localização")
            inserir_carrinho_compras(db, id_carrinho_compras, data_cadastro, 1, id_loja_random)

            cursor.execute("INSERT INTO usuário (idUsuario, Data_Nascimento, Nome, Data_Cadastro, Email, Telefone, ID_Biblioteca, ID_Perfil_Usuário, ID_Carrinho_de_Compras) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", 
                        (data['id'], data['birthdate'], data['name'], data_cadastro, data['email'], data['phone'], id_biblioteca, id_perfil_usuario, id_carrinho_compras))
            db.commit()
            print("Usuário adicionado com sucesso.")
            return jsonify({"message": "Usuário adicionado com sucesso!"}), 201
        except Error as e:
            db.rollback()
            return jsonify({"message": f"Falha ao adicionar usuário: {e}"}), 500
    else:
        return jsonify({"message": "Falha na conexão com o banco de dados."}), 500
    
# Rota para listar usuários
@app.route('/get_users', methods=['GET'])
def get_users():
    db = conexao()
    if db:
        try:
            cursor = db.cursor()
            cursor.execute("SELECT idUsuario, Nome, Email, Data_Nascimento, Telefone FROM usuário")
            users = cursor.fetchall()
            users_list = [{"id": user[0], "name": user[1], "email": user[2], "birthdate": user[3], "phone": user[4]} for user in users]
            return jsonify(users_list), 200
        except Error as e:
            return jsonify({"message": f"Falha ao listar usuários: {e}"}), 500
    else:
        return jsonify({"message": "Falha na conexão com o banco de dados."}), 500

# Rota para editar usuário
@app.route('/edit_user/<int:id>', methods=['PUT'])
def edit_user(id):
    data = request.get_json()
    db = conexao()
    if db:
        try:
            cursor = db.cursor()
            cursor.execute("UPDATE usuário SET Nome = %s, Email = %s, Data_Nascimento = %s, Telefone = %s WHERE idUsuario = %s", 
                           (data['name'], data['email'], data['birthdate'], data['phone'], id))
            db.commit()
            return jsonify({"message": "Usuário atualizado com sucesso!"}), 200
        except Error as e:
            db.rollback()
            return jsonify({"message": f"Falha ao atualizar usuário: {e}"}), 500
    else:
        return jsonify({"message": "Falha na conexão com o banco de dados."}), 500


# Rota para deletar usuário
@app.route('/delete_user/<int:id>', methods=['DELETE'])
def delete_user(id):
    db = conexao()
    if db:
        try:
            cursor = db.cursor()
            cursor.execute("SELECT ID_Biblioteca, ID_Perfil_Usuário, ID_Carrinho_de_Compras FROM usuário WHERE idUsuario = %s", (id,))
            result = cursor.fetchone()

            if result:
                id_biblioteca, id_perfil_usuario, id_carrinho_compras = result

                # Deletar o usuário primeiro
                cursor.execute("DELETE FROM usuário WHERE idUsuario = %s", (id,))
                db.commit()

                # Deletar as chaves estrangeiras associadas
                deletar_biblioteca_jg(db, id_biblioteca)
                deletar_perfil_usuario(db, id_perfil_usuario)
                deletar_carrinho(db, id_carrinho_compras)

                return jsonify({"message": "Usuário deletado com sucesso!"}), 200
            else:
                return jsonify({"message": "Usuário não encontrado."}), 404
        except Error as e:
            db.rollback()
            return jsonify({"message": f"Falha ao deletar usuário: {e}"}), 500
        finally:
            cursor.close()
            db.close()
    else:
        return jsonify({"message": "Falha na conexão com o banco de dados."}), 500



if __name__ == '__main__':
    app.run(debug=True)
