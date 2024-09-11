CREATE DATABASE IF NOT EXISTS plataforma_de_vendas_de_jogos_online;
USE plataforma_de_vendas_de_jogos_online;

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255),
    birthdate DATE,
    phone VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS purchases (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    game_name VARCHAR(255),
    price DECIMAL(10, 2),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE IF NOT EXISTS payments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    game_name VARCHAR(255) NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    payment_type ENUM('PIX', 'Boleto', 'Cartão') NOT NULL,
    payment_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);