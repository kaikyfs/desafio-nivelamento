-- IMPORTANDO DADOS (Processo feito no pgAdmin)
"\\copy public.demonstracoes_contabeis (data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final) 
FROM 'C:/Projetos/TESTEI~1/database/TODOS_~1/4T2023.csv' 
DELIMITER ';' CSV HEADER ENCODING 'LATIN1' QUOTE '\"' ESCAPE '''';""
"\\copy public.operadoras_plano_saude (reg_ans, cnpj, razao_social, nome_fantasia, modalidade, logradouro, numero, complemento, bairro, cidade, uf, cep, ddd, telefone, fax, endereco_eletronico, representante, cargo_representante, regiao_comecializacao, data_registro) 
FROM 'C:/Users/kaiky/DOWNLO~1/RELATO~2.CSV' 
DELIMITER ';' CSV HEADER ENCODING 'LATIN1' QUOTE '\"' ESCAPE '''';"""