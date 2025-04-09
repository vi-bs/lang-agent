from langchain_core.messages import SystemMessage, HumanMessage
from langchain_community.chat_models import ChatOllama

# Use the LLaMA 3 model running on Ollama
llm = ChatOllama(model="llama3")

# Define the message flow
messages = [
    SystemMessage(content="You are an expert in social media content strategy."),
    HumanMessage(content="Give a short tip to create engaging posts on Instagram."),
]

# Run the LLM
response = llm.invoke(messages)

# Print the response
print(response)