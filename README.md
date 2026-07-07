# Offline AI Chatbot

A local AI chatbot built with **Python**, **Streamlit**, and **Ollama**. The application provides an interactive chat interface powered by a locally running Large Language Model (LLM), allowing users to communicate with AI without an internet connection.

## Features

- Offline AI chatbot
- Streamlit chat interface
- Local LLM inference with Ollama
- Conversation history
- Session memory
- Reset chat history
- Loading spinner while generating responses
- Basic prompt filtering
- Persian language support

## Technologies

- Python
- Streamlit
- Ollama
- Requests

## Project Structure

```
offline-ai-chatbot/
├── app.py
├── utils.py
├── requirements.txt
└── README.md
```

## Requirements

Before running the project, make sure you have:

- Python 3.10+
- Ollama installed
- A supported language model (e.g. `qwen2.5-coder:7b`)

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/offline-ai-chatbot.git
```

Navigate to the project folder:

```bash
cd offline-ai-chatbot
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Download the model using Ollama:

```bash
ollama pull qwen2.5-coder:7b
```

Start the Ollama server:

```bash
ollama serve
```

Run the application:

```bash
streamlit run app.py
```

## Features Overview

- Interactive chat interface
- Local inference without cloud APIs
- Conversation memory using Streamlit Session State
- Reset conversation button
- Spinner while AI generates responses
- Simple rule-based filtering for selected topics

## Preview

Add screenshots of:

- Chat interface
- AI responses
- Reset Memory feature

## Future Improvements

- Streaming responses
- Multiple model selection
- Dark mode
- Markdown rendering
- Chat export
- File upload support
- PDF Question Answering
- RAG (Retrieval-Augmented Generation)
- Voice input and speech output

## Contributing

Contributions, suggestions, and improvements are welcome. Feel free to open an issue or submit a pull request.

---

If you found this project useful, consider giving it a ⭐ on GitHub.
