CREATE TABLE alunos (
    id INT PRIMARY KEY,
    nome TEXT,
    idade INT,
    curso TEXT
);

INSERT INTO alunos (id, nome, idade, curso)
VALUES
    (1, 'Aurora', 25, 'Fisioterapia'),
    (2, 'Flora', 22, 'Moda'),
    (3, 'Caio', 28, 'Fisica'),
    (4, 'Gabriela', 21, 'Turismo'),
    (5, 'Marcos', 30, 'Pedagogia');

SELECT * FROM alunos;
SELECT nome, idade FROM alunos WHERE idade > 20;
SELECT * FROM alunos WHERE curso = 'Fisioterapia' ORDER BY nome;
SELECT COUNT(*) FROM alunos;
UPDATE alunos SET idade = 26 WHERE id = 1;
DELETE FROM alunos WHERE id = 3;

CREATE TABLE clientes (
    id INT PRIMARY KEY,
    nome TEXT,
    idade INT,
    saldo FLOAT
);

INSERT INTO clientes (id, nome, idade, saldo)
VALUES
    (101, 'Cliente A', 35, 1500.50),
    (102, 'Cliente B', 28, 2200.75),
    (103, 'Cliente C', 42, 1800.00),
    (104, 'Cliente D', 32, 900.25),
    (105, 'Cliente E', 50, 3500.60);

SELECT nome, idade FROM clientes WHERE idade > 30;
SELECT AVG(saldo) AS saldo_medio FROM clientes;
SELECT nome, MAX(saldo) AS saldo_maximo FROM clientes;
SELECT COUNT(*) AS clientes_com_saldo_acima_de_1000 FROM clientes WHERE saldo > 1000;
UPDATE clientes SET saldo = 1600.75 WHERE id = 101;
DELETE FROM clientes WHERE id = 104;

CREATE TABLE compras (
    id INT PRIMARY KEY,
    cliente_id INT,
    produto TEXT,
    valor REAL
);

INSERT INTO compras (id, cliente_id, produto, valor)
VALUES
    (201, 101, 'Produto X', 50.00),
    (202, 102, 'Produto Y', 75.50),
    (203, 103, 'Produto Z', 120.25),
    (204, 101, 'Produto A', 30.00),
    (205, 105, 'Produto B', 90.75);

SELECT c.nome AS nome_cliente, p.produto, p.valor
FROM compras p
JOIN clientes c ON p.cliente_id = c.id;
