# 🧠 LangAgent — LangChain + Ollama + Chroma RAG with Tools

A modular project demonstrating:

- Retrieval-Augmented Generation (RAG) with metadata
- Local LLM integration using **Ollama + LLaMA 3 (free)**
- Custom agent tool (like getting system time)
- Modular LangChain components: prompts, chains, chat models

---

## 🚀 Features

- 📄 Load and chunk documents
- 🔍 Embed documents using `sentence-transformers`
- 🧠 Store/retrieve embeddings via **ChromaDB**
- 🧠 Use **local LLaMA 3 via Ollama** as the LLM
- 🛠️ Tool-powered LangChain Agent (e.g., current system time)

---

## 🗂️ Project Structure
lang-agent/
├── 1_chat_models/                # Example scripts using LLM chat models
│   └── chat_model_example.py
│
├── 2_prompt_templates/           # Prompt examples
│   ├── prompt_template_1.txt
│   
│
├── 3_chains/                     # Chains combining LLM + tools
│   └── chain_example.py
│
├── 4_Rags/                       # Retrieval-Augmented Generation
│   ├── documents/                # Source text files
│   │   ├── dracula.txt
│   │   └── lord_of_the_rings.txt
│   ├── 1a_basic_part_1.py        # Embedding and saving Chroma vectorstore
│   ├── 2a_rag_basics_metadata.py # Adding source metadata per document
│   └── 3_rag_query_llm.py        # Query vectorstore using Ollama
│
├── 5_agents/                     # LangChain Agent with tools
│   └── 1_agent_time_tool.py      # “Get time” tool using custom @tool
│
├── db/                           # Persistent ChromaDB vectorstore
│   └── chroma_db_with_metadata/
│
├── .gitignore
├── requirements.txt
└── README.md
---

## 🛠️ Setup Instructions

### 1. Install Ollama

You must have Ollama installed with LLaMA 3 pulled:

```bash
# Install Ollama (macOS/Linux/Windows WSL)
https://ollama.com/download

# Pull the free LLaMA 3 model
ollama pull llama3
2. Set up virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
📦 Requirements

Install dependencies:
pip install -r requirements.txt
Example requirements.txt:
langchain
langchain-community
langchain-core
langchainhub
langchain-chroma
sentence-transformers
chromadb
ollama
python-dotenv
🧠 We use sentence-transformers for local embeddings (instead of OpenAI). No API keys needed.
📄 Usage Examples

Embed Documents (1a & 2a)
cd 4_Rags
python 1a_basic_part_1.py
# or for metadata support:
python 2a_rag_basics_metadata.py
Query using Ollama LLaMA 3
python 3_rag_query_llm.py
Use Agent with Tool
cd 5_agents
python 1_agent_time_tool.py

💡 Tips
	•	Store documents inside 4_Rags/documents/
	•	Embeddings are saved in db/chroma_db_with_metadata/
	•	Make sure Ollama is running in the background before querying the LLM

📌 Notes
	•	✅ Uses free local models — No API key required.
	•	✅ Fast prototyping with LangChain
	•	✅ Modular structure for extending with more tools or chains

🙌 Acknowledgements
	•	LangChain
	•	Ollama
	•	ChromaDB
	•	Meta LLaMA 3

📫 Author

Vibha N R
Junior | AI & ML @ New Horizon College of Engineering
GitHub