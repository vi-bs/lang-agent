from langchain_community.chat_models import ChatOllama
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

# Create a ChatOllama model (LLaMA 3 must be running via Ollama)
model = ChatOllama(model="llama3")

chat_history = []  # Use a list to store messages

# Initial system message (optional but helps guide the model)
system_message = SystemMessage(content="You are a helpful AI assistant.")
chat_history.append(system_message)

# Chat loop
while True:
    query = input("You: ")
    if query.lower() == "exit":
        break

    chat_history.append(HumanMessage(content=query))  # User message

    # Get AI response with history
    result = model.invoke(chat_history)
    response = result.content
    chat_history.append(AIMessage(content=response))  # AI message

    print(f"AI: {response}")

# Print conversation history
print("\n---- Message History ----")
for msg in chat_history:
    role = msg.__class__.__name__.replace("Message", "")
    print(f"{role}: {msg.content}")