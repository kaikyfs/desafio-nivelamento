class Operadora:
    def __init__(self, id, reg_ans, cnpj, razao_social, nome_fantasia, modalidade, logradouro, numero, complemento, bairro, cidade, uf, cep, ddd, telefone, fax, endereco_eletronico, representante, cargo_representante, regiao_comecializacao, data_registro) :
        self.id = id
        self.reg_ans = reg_ans
        self.cnpj = cnpj
        self.razao_social = razao_social
        self.nome_fantasia = nome_fantasia
        self.modalidade = modalidade
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.bairro = bairro
        self.cidade = cidade
        self.uf = uf
        self.cep = cep
        self.ddd = ddd
        self.telefone = telefone
        self.fax = fax
        self.endereco_eletronico = endereco_eletronico
        self.representante = representante
        self.cargo_representante = cargo_representante
        self.regiao_comecializacao = regiao_comecializacao
        self.data_registro = data_registro

    def to_dict(self):
            return {
                "id": self.id,
                "reg_ans": self.reg_ans,
                "cnpj": self.cnpj,
                "razao_social": self.razao_social,
                "nome_fantasia": self.nome_fantasia,
                "modalidade": self.modalidade,
                "logradouro": self.logradouro,
                "numero": self.numero,
                "complemento": self.complemento,
                "bairro": self.bairro,
                "cidade": self.cidade,
                "uf": self.uf,
                "cep": self.cep,
                "ddd": self.ddd,
                "telefone": self.telefone,
                "fax": self.fax,
                "endereco_eletronico": self.endereco_eletronico,
                "representante": self.representante,
                "cargo_representante": self.cargo_representante,
                "regiao_comecializacao": self.regiao_comecializacao,
                "data_registro": self.data_registro
            }