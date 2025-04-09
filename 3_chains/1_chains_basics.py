from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain_community.llms import Ollama

# Load environment variables (not strictly needed for Ollama, but kept for consistency)

# Initialize the Ollama LLM with LLaMA 3 model
model = Ollama(model="llama3")

# Define the prompt template
prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a facts expert who knows facts about {animal}."),
        ("human", "Tell me {fact_count} facts."),
    ]
)

# Combine using LangChain Expression Language
chain = prompt_template | model | StrOutputParser()

# Run the chain
result = chain.invoke({"animal": "elephant", "fact_count": 1})

# Output
print(result)