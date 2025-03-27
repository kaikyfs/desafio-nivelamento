# Desafio de Nivelamento - Estágio

Este repositório contém a solução para o desafio de nivelamento para a vaga de estágio. O desafio consiste em quatro testes envolvendo Web Scraping, Transformação de Dados, Banco de Dados e API.

## 📌 Objetivo

Implementar soluções para os seguintes desafios:
1. **Web Scraping**: Coletar e compactar documentos do site da ANS.
2. **Transformação de Dados**: Extrair e formatar tabelas em CSV.
3. **Banco de Dados**: Criar e popular tabelas no MySQL/PostgreSQL e executar consultas analíticas.
4. **API**: Criar um servidor em Python com uma interface em Vue.js.

---

## 🛠 Tecnologias Utilizadas
- **Python** (para Web Scraping e manipulação de dados)
- **BeautifulSoup / Selenium** (para Web Scraping)
- **Pandas** (para tratamento de dados)
- **MySQL / PostgreSQL** (para armazenamento de dados)
- **Flask / FastAPI** (para a API)
- **Vue.js** (para interface web)

---

## 📂 Estrutura do Projeto
```
.
├── web_scraping
│   ├── scraper.py  # Script para baixar os PDFs e compactá-los
│   ├── requirements.txt  # Dependências
│
├── data_transformation
│   ├── transform.py  # Extração e formatação dos dados
│   ├── output.csv  # Dados extraídos e tratados
│
├── database
│   ├── schema.sql  # Scripts para criação de tabelas
│   ├── insert.sql  # Scripts para inserção de dados
│   ├── queries.sql  # Consultas analíticas
│
├── api
│   ├── app.py  # Servidor Flask/FastAPI
│   ├── models.py  # Modelos de dados
│   ├── routes.py  # Rotas da API
│   ├── requirements.txt  # Dependências
│   ├── frontend
│   │   ├── src
│   │   ├── public
│   │   ├── package.json  # Dependências Vue.js
│   │   └── ...
│
└── README.md  # Documento principal
```

---

## 🚀 Como Executar

### 1️⃣ Clonar o Repositório
```bash
git clone https://github.com/seu-usuario/desafio-nivelamento.git
cd desafio-nivelamento
```

### 2️⃣ Web Scraping
```bash
cd web_scraping
pip install -r requirements.txt
python scraper.py
```

### 3️⃣ Transformação de Dados
```bash
cd ../data_transformation
pip install -r requirements.txt
python transform.py
```

### 4️⃣ Configurar o Banco de Dados
```bash
cd ../database
# Criar as tabelas no MySQL/PostgreSQL
mysql -u usuario -p < schema.sql
mysql -u usuario -p < insert.sql
```

### 5️⃣ Executar a API
```bash
cd ../api
pip install -r requirements.txt
python app.py
```
A API estará rodando em `http://localhost:5000`

### 6️⃣ Executar o Frontend
```bash
cd frontend
npm install
npm run serve
```
O frontend estará acessível em `http://localhost:8080`

---

## 📌 Funcionalidades Implementadas
✅ Web Scraping e download dos arquivos PDF.
✅ Extração e transformação de dados para CSV.
✅ Criação e população de banco de dados.
✅ API para consulta de operadoras.
✅ Frontend em Vue.js para exibição dos dados.

---

## 🔗 Referências
- [Portal ANS](https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos)
- [Dados Abertos ANS](https://dadosabertos.ans.gov.br/FTP/PDA/)

---

## 📢 Autor
Desenvolvido por Kaiky Ferreira para a vaga de estágio.

Se tiver dúvidas, entre em contato! 😊

