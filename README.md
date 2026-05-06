# AI-Medical-Assistant
This project is an AI-powered medical assistant built using FastAPI and Groq's LLM (LLaMA 3.1). It provides general medical guidance based on user queries.


⚠️ Disclaimer: This app does NOT replace professional medical advice.

---

## Features
- Ask medical-related questions
- AI-generated safe responses
- Built with FastAPI
- Uses Groq LLM API
- Simple REST API endpoint

---

## Tech Stack
- Python
- FastAPI
- Groq API (LLaMA 3.1)
- Uvicorn

---

## Setup Instructions

### 1. Clone the repo

git clone https://github.com/YOUR_USERNAME/AI-Medical-Assistant.git

cd AI-Medical-Assistant


### 2. Install dependencies

pip install -r requirements.txt


### 3. Add API Key
Create a `.env` file:

GROQ_API_KEY=your_api_key_here


### 4. Run the server

uvicorn main:app --reload


### 5. Open in browser

http://127.0.0.1:8000/docs


---

## API Endpoint

### POST `/ask`

**Request:**

{
"question": "I have a headache, what should I do?"
}


**Response:**

{
"answer": "...",
"disclaimer": "Consult a doctor"
}


---

##  Future Improvements
- Add frontend (React / Streamlit)
- Add symptom checker UI
- Add patient history tracking
- Deploy on Render / Railway

---

## Author
Risha Pinto
