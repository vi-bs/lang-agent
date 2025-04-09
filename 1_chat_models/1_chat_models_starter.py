from langchain_community.llms import Ollama

# Initialize LLaMA 3 model via Ollama
llm = Ollama(model="llama3")

# Ask a question
result = llm.invoke("What is the current time in India?")

# Print the response
print(result)