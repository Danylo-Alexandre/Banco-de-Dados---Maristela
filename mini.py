from flask import Flask, request, jsonify
import mysql.connector
from mysql.connector import Error
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Função para conectar ao banco de dados
def conexao():
    try:
        con_BD = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Gr@n0300',
            database='plataforma_de_vendas_de_jogos_online'
        )
        if con_BD.is_connected():
            return con_BD
    except Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")
        return None

# Rota para adicionar usuário
@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    db = conexao()
    if db:
        try:
            cursor = db.cursor()
            cursor.execute("INSERT INTO users (name, email, birthdate, phone) VALUES (%s, %s, %s, %s)", 
                        (data['name'], data['email'], data['birthdate'], data['phone']))
            db.commit()
            return jsonify({"message": "Usuário adicionado com sucesso!"}), 201
        except Error as e:
            db.rollback()
            return jsonify({"message": f"Falha ao adicionar usuário: {e}"}), 500
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
            cursor.execute("UPDATE users SET name = %s, email = %s, birthdate = %s, phone = %s WHERE id = %s", 
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
            cursor.execute("DELETE FROM users WHERE id = %s", (id,))
            db.commit()
            return jsonify({"message": "Usuário deletado com sucesso!"}), 200
        except Error as e:
            db.rollback()
            return jsonify({"message": f"Falha ao deletar usuário: {e}"}), 500
    else:
        return jsonify({"message": "Falha na conexão com o banco de dados."}), 500

# Rota para listar usuários
@app.route('/get_users', methods=['GET'])
def get_users():
    db = conexao()
    if db:
        try:
            cursor = db.cursor()
            cursor.execute("SELECT id, name, email, birthdate, phone FROM users")
            users = cursor.fetchall()
            users_list = [{"id": user[0], "name": user[1], "email": user[2], "birthdate": user[3], "phone": user[4]} for user in users]
            return jsonify(users_list), 200
        except Error as e:
            return jsonify({"message": f"Falha ao listar usuários: {e}"}), 500
    else:
        return jsonify({"message": "Falha na conexão com o banco de dados."}), 500

# Rota para listar os jogos comprados de um usuário
@app.route('/get_purchased_games/<int:user_id>', methods=['GET'])
def get_purchased_games(user_id):
    db = conexao()
    if db:
        try:
            cursor = db.cursor()
            cursor.execute("SELECT game_name, price FROM purchases WHERE user_id = %s", (user_id,))
            purchases = cursor.fetchall()
            games_list = [{"game_name": game[0], "price": game[1]} for game in purchases]
            return jsonify(games_list), 200
        except Error as e:
            return jsonify({"message": f"Falha ao buscar jogos comprados: {e}"}), 500
    else:
        return jsonify({"message": "Falha na conexão com o banco de dados."}), 500

# Rota para comprar jogo
@app.route('/buy_game', methods=['POST'])
def buy_game():
    data = request.get_json()
    db = conexao()
    if db:
        try:
            cursor = db.cursor()
            cursor.execute("INSERT INTO purchases (user_id, game_name, price) VALUES (%s, %s, %s)", 
                        (data['user_id'], data['game_name'], data['price']))
            
            # Registrar pagamento
            cursor.execute("INSERT INTO payments (user_id, game_name, amount, payment_type) VALUES (%s, %s, %s, %s)", 
                        (data['user_id'], data['game_name'], data['price'], data['payment_type']))
            
            db.commit()
            return jsonify({"message": "Jogo comprado com sucesso!"}), 201
        except Error as e:
            db.rollback()
            return jsonify({"message": f"Falha ao registrar compra: {e}"}), 500
    else:
        return jsonify({"message": "Falha na conexão com o banco de dados."}), 500

# Rota para listar pagamentos de um usuário
@app.route('/get_payments/<int:user_id>', methods=['GET'])
def get_payments(user_id):
    db = conexao()
    if db:
        try:
            cursor = db.cursor()
            cursor.execute("SELECT game_name, amount, payment_type, payment_date FROM payments WHERE user_id = %s", (user_id,))
            payments = cursor.fetchall()
            payments_list = [{"game_name": payment[0], "amount": payment[1], "payment_type": payment[2], "payment_date": payment[3]} for payment in payments]
            return jsonify(payments_list), 200
        except Error as e:
            return jsonify({"message": f"Falha ao buscar pagamentos: {e}"}), 500
    else:
        return jsonify({"message": "Falha na conexão com o banco de dados."}), 500

if __name__ == '__main__':
    app.run(debug=True)
