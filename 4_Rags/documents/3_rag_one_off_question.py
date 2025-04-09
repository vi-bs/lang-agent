import os

from langchain_chroma import Chroma
from langchain_community.llms import Ollama
from langchain_community.embeddings import HuggingFaceEmbeddings

# Set the persistent directory
current_dir = os.path.dirname(os.path.abspath(__file__))
persistent_directory = os.path.join(current_dir, "db", "chroma_db_with_metadata")

# Use HuggingFace Embeddings (local)
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Load existing vector store
if not os.path.exists(persistent_directory):
    raise FileNotFoundError(f"❌ Chroma vector store not found at: {persistent_directory}")

db = Chroma(persist_directory=persistent_directory, embedding_function=embeddings)

# User query
query = "What does dracula fear the most?"

# Retrieve relevant documents
retriever = db.as_retriever(search_type="similarity", search_kwargs={"k": 3})
relevant_docs = retriever.invoke(query)

# Show retrieved documents
print("\n--- 📄 Relevant Documents ---")
for i, doc in enumerate(relevant_docs, 1):
    print(f"\n📄 Document {i}:\n{doc.page_content}")
    if doc.metadata:
        print(f"🔗 Source: {doc.metadata.get('source', 'Unknown')}")

# Combine input for the LLM
combined_input = (
    f"Based on the following documents, answer the question: '{query}'\n\n"
    + "\n\n".join([doc.page_content for doc in relevant_docs])
    + "\n\nIf the answer isn't in the documents, say: 'I'm not sure'."
)

# Load Ollama LLM (LLaMA 3)
llm = Ollama(model="llama3")

# Get the result
response = llm.invoke(combined_input)

# Display the result
print("\n--- 🤖 LLaMA 3 Response ---")
print(response)