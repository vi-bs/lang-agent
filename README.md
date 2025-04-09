# 🧠 LangChain Agent Integrations with Ollama LLaMA 3

This repository showcases various implementations and integrations using **LangChain**, focusing on chat models, prompt templates, chains, Retrieval-Augmented Generation (RAG), and agent-based systems. It leverages **free, open-source models** like **Ollama's LLaMA 3** for all LLM-related functionality.

---

## 🚀 Features

- **🔁 RAG with Metadata Support**
  - Document loading, chunking, and embedding
  - Vector storage with ChromaDB
  - Query answering based on retrieved context

- **🛠️ Agent Execution with Tools**
  - REACT-style agent integrated with LangChain Tools
  - Example tool: system time retriever

- **💬 LLM Integration (Ollama)**
  - Uses Ollama's local LLaMA 3 model
  - No OpenAI or cloud dependency

- **📄 Prompt Templates and Chains**
  - Custom prompts for guided reasoning
  - Chains to link retrieval, formatting, and generation

---

## 🏗️ Project Structure

```
lang-agent/
├── documents/                     # Input text files for document-based RAG
│   ├── dracula.txt
│   └── ...
│
├── db/                           # Vector DB persistence directories
│   ├── chroma_db/                # Basic RAG
│   └── chroma_db_with_metadata/  # Metadata-aware RAG
│
├── agents/                       # Agent-related code
│   └── agent_with_tools.py       # REACT agent with custom tools
│
├── rag/                          # RAG scripts
│   ├── 1a_basic_part_1.py        # Basic RAG - chunking and vector DB init
│   ├── 1b_query_part_2.py        # Basic RAG - query from existing DB
│   ├── 2a_rag_basics_metadata.py # RAG with file metadata
│   └── 2b_rag_query_metadata.py  # Query from metadata-based RAG
│
├── .env                          # Environment variables (optional)
├── requirements.txt              # Python dependencies
└── README.md                     # Project documentation
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/vi-bs/lang-agent.git
cd lang-agent
```

### 2. Set Up Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # For Mac/Linux
venv\Scripts\activate     # For Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Ollama and LLaMA 3

> 🧠 Make sure you have Ollama installed. You can get it from: https://ollama.com

Then pull the LLaMA 3 model:

```bash
ollama pull llama3
```

---

## ✅ Running the Examples

### Basic RAG Initialization
```bash
python rag/1a_basic_part_1.py
```
### Querying the RAG Vector Store
```bash
python rag/1b_query_part_2.py
```

### Metadata-Based RAG Initialization
```bash
python rag/2a_rag_basics_metadata.py
```
### Querying with Metadata-Based RAG
```bash
python rag/2b_rag_query_metadata.py
```

### Running the Agent with Tools
```bash
python agents/agent_with_tools.py
```

---

## 🧪 Example Agent Query

> **Input**: "What is the current time in London? (You are in India)"
>
> **Tool Used**: get_system_time

---

## 📜 License
MIT License

---

## 🙌 Acknowledgments
- [LangChain](https://github.com/langchain-ai/langchain)
- [Ollama](https://ollama.com)
- [Chroma](https://github.com/chroma-core/chroma)
- [LLaMA 3 by Meta](https://ai.meta.com/llama/)

---

## 💡 Future Enhancements
- Add support for document upload via UI
- Integrate LangGraph workflows
- Experiment with custom Ollama models and embeddings

