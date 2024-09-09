-- -----------------------------------------------------
-- Banco de Dados Plataforma de vendas de jogos online
-- -----------------------------------------------------
 CREATE DATABASE Plataforma_de_vendas_de_jogos_online;
 USE Plataforma_de_vendas_de_jogos_online;

-- -----------------------------------------------------
-- Tabela Jogo
-- -----------------------------------------------------
CREATE TABLE Jogo (

  idJogo INT NOT NULL,
  Descrição VARCHAR(45) NOT NULL,
  Titulo VARCHAR(45) NOT NULL,
  Categoria VARCHAR(45) NOT NULL,
  Data_Lancamento DATE NOT NULL,
  Capa BLOB NULL,
  Processador VARCHAR(45) NOT NULL,
  Memoria_RAM VARCHAR(45) NOT NULL,
  Placa_de_Vídeo VARCHAR(45) NOT NULL,
  Armazenamento VARCHAR(45) NOT NULL,
  PRIMARY KEY (idJogo)
);


-- -----------------------------------------------------
-- Tabela Biblioteca_de_Jogos
-- -----------------------------------------------------
CREATE TABLE Biblioteca_de_Jogos (

  idBiblioteca_de_Jogos INT NOT NULL,
  Status_Instalação INT NOT NULL,
  Data_de_Adição DATE NOT NULL,
  PRIMARY KEY (idBiblioteca_de_Jogos)
);

-- -----------------------------------------------------
-- Tabela Perfil_Usuário
-- -----------------------------------------------------
CREATE TABLE Perfil_Usuário (

  idPerfil_Usuário INT NOT NULL,
  Foto_perfil BLOB NULL,
  Biografia VARCHAR(45) NOT NULL,
  Localização VARCHAR(45) NOT NULL,
  PRIMARY KEY (idPerfil_Usuário)
);


-- -----------------------------------------------------
-- Tabela Loja
-- -----------------------------------------------------
CREATE TABLE Loja (

  idLoja INT NOT NULL,
  Preço VARCHAR(45) NOT NULL,
  ID_Jogo INT NOT NULL,
  PRIMARY KEY (idLoja),
  
  CONSTRAINT Chave_Estrangeira_Loja_Jogo
    FOREIGN KEY (ID_Jogo)
    REFERENCES Jogo (idJogo)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
);


-- -----------------------------------------------------
-- Tabela Carrinho_de_Compras
-- -----------------------------------------------------
CREATE TABLE Carrinho_de_Compras (

  idCarrinho_de_Compras INT NOT NULL,
  Data_de_Adição DATE NOT NULL,
  Quantidade INT NOT NULL,
  ID_Loja INT NOT NULL,
  PRIMARY KEY (idCarrinho_de_Compras),
  
  CONSTRAINT Chave_Estrangeira_Carrinho_de_Compras_Loja
    FOREIGN KEY (ID_Loja)
    REFERENCES Loja (idLoja)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
);


-- -----------------------------------------------------
-- Tabela Usuário
-- -----------------------------------------------------
CREATE TABLE Usuário (

  idUsuario INT NOT NULL,
  Data_Nascimento DATE NOT NULL,
  Nome VARCHAR(45) NOT NULL,
  Data_Cadastro VARCHAR(45) NOT NULL,
  Email VARCHAR(45) NOT NULL,
  Telefone VARCHAR(20) NULL,
  ID_Biblioteca INT NOT NULL,
  ID_Perfil_Usuário INT NOT NULL,
  ID_Carrinho_de_Compras INT NOT NULL,
  PRIMARY KEY (idUsuario),

  CONSTRAINT Chave_Estrangeira_Usuario_Biblioteca_de_Jogos
    FOREIGN KEY (ID_Biblioteca)
    REFERENCES Biblioteca_de_Jogos (idBiblioteca_de_Jogos)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT Chave_Estrangeira_Perfil_Usuário
    FOREIGN KEY (ID_Perfil_Usuário)
    REFERENCES Perfil_Usuário (idPerfil_Usuário)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT Chave_Estrangeira_Usuário_CaDC
    FOREIGN KEY (ID_Carrinho_de_Compras)
    REFERENCES Carrinho_de_Compras (idCarrinho_de_Compras)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
    );


-- -----------------------------------------------------
-- Tabela Usuário_possui_Jogo
-- -----------------------------------------------------
CREATE TABLE Usuário_possui_Jogo (

  ID_Usuário INT NOT NULL,
  ID_Jogo INT NOT NULL,
  PRIMARY KEY (ID_Usuário, ID_Jogo),

  CONSTRAINT Chave_Estrangeira_Usuario_possui_Jogo_Tabela_U
    FOREIGN KEY (ID_Usuário )
    REFERENCES Usuário (idUsuario)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT Chave_Estrangeira_Usuário_possui_Jogo_Tabela_J
    FOREIGN KEY (ID_Jogo)
    REFERENCES Jogo (idJogo)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
);


-- -----------------------------------------------------
-- Tabela Biblioteca_de_Jogos_possui_Jogo
-- -----------------------------------------------------
CREATE TABLE Biblioteca_de_Jogos_possui_Jogo (

  ID_Biblioteca INT NOT NULL,
  ID_Jogo INT NOT NULL,
  PRIMARY KEY (ID_Biblioteca, ID_Jogo),

  CONSTRAINT Chave_Estrangeira_Biblioteca_de_Jogos_possui_Jogo_Tabela_Bi
    FOREIGN KEY (ID_Biblioteca)
    REFERENCES Biblioteca_de_Jogos (idBiblioteca_de_Jogos)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT Chave_Estrangeira_Biblioteca_de_Jogos_possui_Jogo_Tabela_J
    FOREIGN KEY (ID_Jogo)
    REFERENCES Jogo (idJogo)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
);


-- -----------------------------------------------------
-- Tabela Avaliação
-- -----------------------------------------------------
CREATE TABLE Avaliação (

  idAvaliação INT NOT NULL,
  Nota INT NOT NULL,
  Comentário VARCHAR(45) NOT NULL,
  PRIMARY KEY (idAvaliação)
);


-- -----------------------------------------------------
-- Tabela Jogo_possui_Avaliação
-- -----------------------------------------------------
CREATE TABLE Jogo_possui_Avaliação (

  ID_Jogo INT NOT NULL,
  ID_Avaliação INT NOT NULL,
  PRIMARY KEY (ID_Jogo, ID_Avaliação),

  CONSTRAINT Chave_Estrangeira_Jogo_possui_Avaliação_Tabela_J
    FOREIGN KEY (ID_Jogo)
    REFERENCES Jogo (idJogo)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT Chave_Estrangeira_Jogo_possui_Avaliação_Tabela_A
    FOREIGN KEY (ID_Avaliação)
    REFERENCES Avaliação (idAvaliação)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
);


-- -----------------------------------------------------
-- Tabela Desenvolvedor
-- -----------------------------------------------------
CREATE TABLE Desenvolvedor (

  idDesenvolvedor INT NOT NULL,
  Nome VARCHAR(45) NOT NULL,
  Telefone VARCHAR(20) NOT NULL,
  Email VARCHAR(45) NOT NULL,
  ID_Perfil_Usuário INT NOT NULL,
  PRIMARY KEY (idDesenvolvedor),

  CONSTRAINT Chave_Estrangeira_Deselvolvedor_Perfil_U
    FOREIGN KEY (ID_Perfil_Usuário)
    REFERENCES Perfil_Usuário (idPerfil_Usuário)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
);


-- -----------------------------------------------------
-- Tabela Deselvolvedor_possui_Jogo
-- -----------------------------------------------------
CREATE TABLE Deselvolvedor_possui_Jogo (

  ID_Desenvolvedor INT NOT NULL,
  ID_Jogo INT NOT NULL,
  PRIMARY KEY (ID_Desenvolvedor, ID_Jogo),

  CONSTRAINT Chave_Estrangeira_Deselvolvedor_possui_Jogo_Tabela_D
    FOREIGN KEY (ID_Desenvolvedor)
    REFERENCES Desenvolvedor (idDesenvolvedor)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT Chave_Estrangeira_Deselvolvedor_possui_Jogo_Tabela_J
    FOREIGN KEY (ID_Jogo)
    REFERENCES Jogo (idJogo)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
);


-- -----------------------------------------------------
-- Tabela Suporte
-- -----------------------------------------------------
CREATE TABLE Suporte (

  Protocolo INT NOT NULL,
  Problema VARCHAR(45) NOT NULL,
  Data_Solicitação DATE NOT NULL,
  Resposta VARCHAR(20) NOT NULL,
  PRIMARY KEY (Protocolo)
);


-- -----------------------------------------------------
-- Tabela Usuário_solicita_Suporte
-- -----------------------------------------------------
CREATE TABLE Usuário_solicita_Suporte (

  ID_Usuário INT NOT NULL,
  ID_Suporte INT NOT NULL,
  PRIMARY KEY (ID_Usuário, ID_Suporte),

  CONSTRAINT Chave_Estrangeira_Usuário_solicita_Suporte_Tabela_U
    FOREIGN KEY (ID_Usuário)
    REFERENCES Usuário (idUsuario)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT Chave_Estrangeira_Usuário_solicita_Suporte_Tabela_S
    FOREIGN KEY (ID_Suporte)
    REFERENCES Suporte (Protocolo)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
);


-- -----------------------------------------------------
-- Tabela Sistema_Operacional
-- -----------------------------------------------------
CREATE TABLE Sistema_Operacional (
  
  IP VARCHAR(45) NOT NULL,
  Nome VARCHAR(45) NOT NULL,
  Versão VARCHAR(45) NOT NULL,
  Fabricante VARCHAR(45) NOT NULL,
  Data_Lançamento DATE NOT NULL,
  PRIMARY KEY (IP)
);


-- -----------------------------------------------------
-- Tabela Usuário_possui_Sistema_Operacional
-- -----------------------------------------------------
CREATE TABLE Usuário_possui_Sistema_Operacional (

  ID_Usuário INT NOT NULL,
  ID_Sistema_Operacional VARCHAR(45) NOT NULL,
  PRIMARY KEY (ID_Usuário, ID_Sistema_Operacional),

  CONSTRAINT Chave_Estrangeira_Usuário_possui_Sistema_Operacional_Tabela_U
    FOREIGN KEY (ID_Usuário)
    REFERENCES Usuário (idUsuario)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT Chave_Estrangeira_Usuário_possui_Sistema_Operacional_Tabela_SO
    FOREIGN KEY (ID_Sistema_Operacional)
    REFERENCES Sistema_Operacional (IP)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
);

-- -----------------------------------------------------
-- Tabela Pagamento
-- -----------------------------------------------------
CREATE TABLE Pagamento (

  idPagamento INT NOT NULL,
  Tipo_Pagamento VARCHAR(45) NOT NULL,
  Status_Pagamento VARCHAR(20) NOT NULL,
  Data_Pagamento DATE NOT NULL,
  ID_Carrinhos_de_Compras INT NOT NULL,
  PRIMARY KEY (idPagamento),

  CONSTRAINT Chave_Estrangeira_Pagamento_Carrinho_de_Compras
    FOREIGN KEY (ID_Carrinhos_de_Compras)
    REFERENCES Carrinho_de_Compras (idCarrinho_de_Compras)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
)
