-- QUERY ANALITICAS

-- Quais as 10 operadoras com maiores despesas em "EVENTOS/ SINISTROS CONHECIDOS OU
-- AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR" no último trimestre?
SELECT 
    d.reg_ans, 
    o.nome_fantasia, 
    SUM(d.vl_saldo_final - d.vl_saldo_inicial) AS total_despesas
FROM 
    demonstracoes_contabeis d
JOIN 
    operadoras_plano_saude o ON d.reg_ans = o.reg_ans
WHERE 
    d.descricao = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR '
    AND d.data >= DATE_TRUNC('quarter', CURRENT_DATE) - INTERVAL '3 months'
GROUP BY 
    d.reg_ans, o.nome_fantasia
ORDER BY 
    total_despesas DESC
LIMIT 10;

-- Quais as 10 operadoras com maiores despesas nessa categoria no último ano?
SELECT 
    d.reg_ans, 
    o.nome_fantasia, 
    SUM(d.vl_saldo_final - d.vl_saldo_inicial) AS total_despesas
FROM 
    demonstracoes_contabeis d
JOIN 
    operadoras_plano_saude o ON d.reg_ans = o.reg_ans
WHERE 
    d.descricao = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR '
    AND d.data >= DATE_TRUNC('year', CURRENT_DATE) - INTERVAL '1 year'
GROUP BY 
    d.reg_ans, o.nome_fantasia
ORDER BY 
    total_despesas DESC
LIMIT 10;
