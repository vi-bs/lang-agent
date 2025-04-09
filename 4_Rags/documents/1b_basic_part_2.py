import os
from langchain_chroma import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

# Set the current working directory and persistent DB location
current_dir = os.path.dirname(os.path.abspath(__file__))
persistent_directory = os.path.join(current_dir, "db", "chroma_db")

# Use Hugging Face Embeddings
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Check if the vector store exists
if not os.path.exists(persistent_directory):
    raise FileNotFoundError(
        f"❌ Chroma vector store not found at {persistent_directory}. Please initialize it first."
    )

# Load the existing Chroma vector store
db = Chroma(persist_directory=persistent_directory, embedding_function=embeddings)

# Define the query
query = "Where does Gandalf meet Frodo?"

# Set up the retriever (without threshold)
retriever = db.as_retriever(
    search_type="similarity",  # removed 'similarity_score_threshold'
    search_kwargs={"k": 5},    # return top 5 most similar chunks
)

# Run retrieval
relevant_docs = retriever.invoke(query)

# Display the results
print("\n--- 📄 Relevant Documents ---")
if not relevant_docs:
    print("❌ No documents found.")
else:
    for i, doc in enumerate(relevant_docs, 1):
        print(f"\n📄 Document {i}:")
        print(doc.page_content)
        if doc.metadata:
            print(f"🔗 Source: {doc.metadata.get('source', 'Unknown')}")