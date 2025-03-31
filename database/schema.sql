-- CRIANDO TABELAS

CREATE TABLE despesas_operadoras (
    id SERIAL PRIMARY KEY,
    data_movimentacao DATE,
    reg_ans INT,
    cd_conta_contabil VARCHAR(20),
    descricao TEXT,
    saldo_inicial DECIMAL(10,2),
    saldo_final DECIMAL(10,2),
);

CREATE TABLE operadoras_plano_saude (
    id SERIAL PRIMARY KEY,
    reg_ans INT,
    cnpj VARCHAR(20),
    razao_social TEXT,
    nome_fantasia TEXT,
    modalidade TEXT,
    logradouro TEXT,
    numero INT,
    complemento TEXT,
    bairro TEXT,
    cidade TEXT,
    uf CHAR(2),
    cep CHAR(8),
    ddd CHAR(2),
    telefone CHAR(9),
    fax CHAR(9),
    endereco_eletronico TEXT,
    representante TEXT,
    cargo_representante TEXT,
    regiao_comecializacao INT,
    data_registro DATE,
)