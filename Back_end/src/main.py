import os
import re
import nltk
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger') 
nltk.download('taggers')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline, AutoModelForSequenceClassification, AutoTokenizer
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
frontend_path = os.path.join(os.path.dirname(__file__), "../../Front_end")

if not os.path.exists(frontend_path):
    raise RuntimeError(f"Pasta Front_end não encontrada em: {frontend_path}")

app.mount("/Front_end", StaticFiles(directory=frontend_path), name="Front_end")

MODEL_NAME = "distilbert-base-uncased-finetuned-sst-2-english"
classifier = pipeline(
   "text-classification",
    model=AutoModelForSequenceClassification.from_pretrained(MODEL_NAME),
    tokenizer=AutoTokenizer.from_pretrained(MODEL_NAME)
)

MODEL_GENERATOR = "google/flan-t5-large"
generator = pipeline("text2text-generation", model=MODEL_GENERATOR)


stop_words = set(stopwords.words('English')) 


class EmailInput(BaseModel):
   
    email_text: str

class EmailOutput(BaseModel):

    classification: str
    suggested_response: str


def preprocess_text(text: str) -> str:
 
    text = text.lower()

    text = re.sub(r'[^a-z\s]', '', text)
 
    tokens = word_tokenize(text)

    filtered_tokens = [w for w in tokens if not w in stop_words and len(w) > 1]

    return " ".join(filtered_tokens)

def classify_productivity(processed_text: str) -> str:
  
    try:
        result = classifier(processed_text)[0]
        label = result['label'].lower()
       
        if "negative" in label:
            return "Improdutivo"
        else:
            return "Produtivo"
        
    except Exception as e:
        print(f"Erro na classificação: {e}")
        return "Indeterminado"

def generate_response(classification: str, original_email: str) -> str:
    
    if classification == "Produtivo":
        prompt = (
            f"O seguinte e-mail foi classificado como PRODUTIVO. "
            f"Gere uma resposta profissional, concisa e de acompanhamento. "
            f"E-mail: '{original_email}'"
        )
    elif classification == "Improdutivo":
        prompt = (
            f"O seguinte e-mail foi classificado como IMPRODUTIVO ou SPAM. "
            f"Gere uma resposta educada e formal que decline a solicitação ou que a encaminhe para o canal correto. "
            f"E-mail: '{original_email}'"
        )
    else:
        return "Não foi possível gerar uma resposta automática devido à classificação indeterminada."

    try:
       response = generator(prompt, max_new_tokens=150)[0]["generated_text"]
       return response.strip()
    except Exception as e:
        return f"Erro ao gerar resposta: {e}"


@app.post("/process_email/", response_model=EmailOutput)
async def process_email(email: EmailInput):

    original_text = email.email_text
    
    processed_text = preprocess_text(original_text)
    
    classification_result = classify_productivity(processed_text)
    
    suggested_response = generate_response(classification_result, original_text)
    

    return EmailOutput(
        classification=classification_result,
        suggested_response=suggested_response
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


@app.get("/", response_class=HTMLResponse)
async def serve_home():
    file_path = os.path.join("Front_end", "Index.html")
    with open(file_path, "r", encoding="utf-8") as f:
        html_content = f.read()
    return html_content