from langchain_community.llms import Ollama
from google.cloud import firestore
from langchain_google_firestore import FirestoreChatMessageHistory
# Initialize LLaMA 3 model via Ollama
model= Ollama(model="llama3")
PROJECT_ID = "langchain-vibs"
SESSION_ID = "user_session_new"  # This could be a username or a unique ID
COLLECTION_NAME = "chat_history"

# Initialize Firestore Client
print("Initializing Firestore Client...")
client = firestore.Client(project=PROJECT_ID)

# Initialize Firestore Chat Message History
print("Initializing Firestore Chat Message History...")
chat_history = FirestoreChatMessageHistory(
    session_id=SESSION_ID,
    collection=COLLECTION_NAME,
    client=client,
)
print("Chat History Initialized.")
print("Current Chat History:", chat_history.messages)

# Initialize Chat Model


print("Start chatting with the AI. Type 'exit' to quit.")

while True:
    human_input = input("User: ")
    if human_input.lower() == "exit":
        break

    chat_history.add_user_message(human_input)

    ai_response = model.invoke(chat_history.messages)
    chat_history.add_ai_message(ai_response)

    print(f"AI: {ai_response}")