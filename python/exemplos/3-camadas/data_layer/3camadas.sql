BEGIN TRANSACTION;
CREATE TABLE venda (
	id INTEGER NOT NULL, 
	desconto NUMERIC, 
	data_hora DATETIME, 
	PRIMARY KEY (id)
);
CREATE TABLE produto (
	id INTEGER NOT NULL, 
	nome VARCHAR, 
	valor_custo NUMERIC, 
	valor_venda NUMERIC, 
	PRIMARY KEY (id)
);
CREATE TABLE item_venda (
	produto_id INTEGER NOT NULL, 
	venda_id INTEGER NOT NULL, 
	quantidade FLOAT, 
	PRIMARY KEY (produto_id, venda_id), 
	FOREIGN KEY(produto_id) REFERENCES produto (id), 
	FOREIGN KEY(venda_id) REFERENCES venda (id)
);
COMMIT;
