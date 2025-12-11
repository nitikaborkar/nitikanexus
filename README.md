#  NitikaNexus - AI-Powered Personal Portfolio Chatbot

[![Live Demo](https://img.shields.io/badge/demo-live-brightgreen)](https://nitkanexus.vercel.app/)
[![React](https://img.shields.io/badge/React-18+-blue.svg)](https://reactjs.org/)
[![Python](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0-black.svg)](https://flask.palletsprojects.com/)

NitikaNexus is an intelligent conversational AI application that provides an interactive way to explore my professional background, technical skills, and getting to know me:) through natural language conversations powered by OpenAI and LangChain.

## Live Demo

**[View Application](https://nitkanexus.vercel.app/)**

> **Note:** Initial responses may take 5-10 seconds as the application uses free-tier hosting services. The backend is currently not hosted due to cost constraints.

---

## Features

- **Intelligent Q&A**: Natural language processing to answer questions about my skills, experience, and projects
- **Context-Aware Responses**: RAG (Retrieval-Augmented Generation) architecture for accurate, context-driven answers
- **Interactive UI**: Clean, responsive React-based interface
- **Real-time Processing**: Seamless integration between frontend and backend APIs
- **Personalized Experience**: Custom-trained on my portfolio data and professional information

---

## Tech Stack

### Frontend
- **Framework**: React.js 18+
- **Deployment**: Vercel
- **Styling**: Modern CSS with responsive design

### Backend
- **Framework**: Flask 3.0 (Python 3.12)
- **AI/ML**: 
  - OpenAI GPT API
  - LangChain for orchestration
  - FAISS for vector embeddings
  - RAG pipeline for knowledge retrieval
- **Deployment**: Heroku (currently offline)

### APIs & Services
- OpenAI API for language model
- LangChain for agent-based workflows
- Custom vector store for knowledge base

---

## 🏗️ Architecture

```
┌─────────────┐ HTTP/REST ┌──────────────┐
│ React │ ◄─────────────────► │ Flask │
│ Frontend │ │ Backend │
│ (Vercel) │ │ (Heroku) │
└─────────────┘ └──────────────┘
│
▼
┌──────────────┐
│ OpenAI │
│ LangChain │
│ FAISS DB │
└──────────────┘
```

## 🚦 Getting Started

### Prerequisites
- Node.js 18+ and npm
- Python 3.12+
- OpenAI API key

### Installation

#### Frontend Setup

```bash
cd frontend
npm install
npm start
```

#### Backend Setup

```
cd backend
pip install -r requirements.txt
python app.py
```

### Environment Variables

Create `.env` files in respective directories:

**Backend `.env`:**
```
OPENAI_API_KEY=your_openai_key
LANGCHAIN_API_KEY=your_langchain_key
FLASK_ENV=development
```


## Usage

1. Navigate to the live application or run locally
2. Type questions about my background, skills, or projects
3. Receive AI-generated responses based on my professional data
4. Explore different aspects of my profile through natural conversation

---

## Future Enhancements

- [ ] Deploy backend to Render/Railway for continuous availability
- [ ] Add conversation history persistence
- [ ] Implement multi-modal support (images, documents)
- [ ] Enhanced analytics dashboard
- [ ] Voice interaction capabilities

---

## Contact

**Nitika Borkar**  
- LinkedIn: [linkedin.com/in/nitikaborkar](https://linkedin.com/in/nitikaborkar)
- Email: nitika.borkar@example.com
- Portfolio: [nitkanexus.vercel.app](https://nitkanexus.vercel.app/)

---

## License

This project is private and intended for portfolio demonstration purposes.

---

**⭐  If you find this project interesting, feel free to star the repository!**
