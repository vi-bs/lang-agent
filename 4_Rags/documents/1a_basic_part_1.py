import os
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_chroma import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

def get_absolute_path(*relative_path):
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), *relative_path)

# Paths
document_name = "lord_of_the_rings.txt"
file_path = get_absolute_path( document_name)
persistent_directory = get_absolute_path("db", "chroma_db")

# Check if Chroma DB exists
if not os.path.exists(persistent_directory):
    print("🔄 Persistent directory not found. Initializing vector store...")

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"❌ File not found: {file_path}")

    # Load document
    loader = TextLoader(file_path)
    documents = loader.load()

    # Split into chunks
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=50)
    docs = text_splitter.split_documents(documents)

    print(f"✅ Loaded and split {len(docs)} chunks.")
    print(f"🔍 Sample chunk:\n{docs[0].page_content}\n")

    # Hugging Face Embeddings
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    print("✨ Hugging Face embeddings initialized.")

    # Vector Store
    db = Chroma.from_documents(docs, embeddings, persist_directory=persistent_directory)
    print("✅ Vector store created and saved.")
else:
    print("✅ Vector store already exists.")

# ---------------------
# Placeholder for queries:
# To do: Add retriever or QA chain here for asking questions.
# Example questions:
#   - "Who is the Ring-bearer?"
#   - "Where does Gandalf meet Frodo?"