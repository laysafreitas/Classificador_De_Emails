# 📧 Classificador de E-mails com IA

Aplicação que utiliza **Inteligência Artificial (IA)** para classificar e-mails como **Produtivos** ou **Improdutivos**, além de gerar uma **resposta automática** com base na categoria detectada.  
Desenvolvido com **FastAPI**, **Transformers (Hugging Face)** e uma interface **HTML/CSS/JavaScript** simples.

---

## 🚀 Funcionalidades

✅ Classifica e-mails como **Produtivos** ou **Improdutivos**  
✅ Gera respostas automáticas com base na classificação  
✅ Interface web intuitiva para envio de e-mails  
✅ Integração entre **Front-end e API FastAPI**  
✅ Suporte a CORS para comunicação entre cliente e servidor  

---

## 🧠 Tecnologias Utilizadas

**Back-end:**
- 🐍 Python 3.10+
- ⚡ FastAPI
- 🤗 Transformers (Hugging Face)
- 🧩 NLTK
- 🧠 Modelos: `distilbert-base-uncased-finetuned-sst-2-english` e `google/flan-t5-base`

**Front-end:**
- 🌐 HTML5, CSS3, JavaScript
- 📁 Deploy opcional via **Vercel** ou **Netlify**

---

## ⚙️ Como Executar o Projeto Localmente

### 🔹 1. Clone o repositório

```bash
git clone https://github.com/laysafreitas/Classificador_De_Emails.git
cd Classificador_De_Emails
```
### 🔹 2. Crie e ative um ambiente virtual

Windows:
```bash
python -m venv venv
venv\Scripts\activate
```
Linux/Mac:
```bash
python3 -m venv venv
source venv/bin/activate
```
### 🔹 3. Instale as dependências

```bash
pip install -r requirements.txt
```
### 🔹 4. Execute o servidor FastAPI

```bash
python -m uvicorn main:app --reload
```

### 🔹 5. Acesse a interface web

- instale a instancia Live server
- Click com o botao direito no arquivo HTML
- escolha a opcao Open in Defauld Browser

## 🧩 Estrutura de Pastas

```css
Classificador_De_Emails/
│
├── Backend/
│   ├── main.py
│   ├── requirements.txt
│   └── ...
│
├── Front_end/
│   ├── Index.html
│   ├── Email.css
│   └── script.js
│
├── README.md
└── LICENSE
```

## 🧪 Exemplo de Uso

### ✉️ Entrada:
```lua
Assunto: Urgente - Reunião de status do projeto

Prezados,
Gostaria de confirmar se a reunião de acompanhamento será mantida para amanhã às 10h.
```
### 🧩 Saída esperada:
```lua
Classificação: Produtivo
Resposta sugerida: Prezado, confirmamos a reunião para amanhã às 10h. Agradecemos o contato.
```

## 🛠️ Possíveis Melhorias Futuras

 - Substituir modelo de sentimento por um modelo treinado para produtividade real

 - Adicionar autenticação e histórico de e-mails processados

 - Criar dashboard para análise das classificações

 - Implementar armazenamento em banco de dados (MongoDB)

## 📄 Licença
Este projeto está licenciado sob a MIT License

## 👩‍💻 Autora
###Laysa Freitas
- 💼 Desenvolvedora Backend | Entusiasta em IA e FastAPI
- 📧 Contato: [Seu e-mail ou LinkedIn]







