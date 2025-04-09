from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
# Initialize LLaMA 3 model via Ollama
llm = Ollama(model="llama3")
messages = [
    ("system", "You are a comedian who tells jokes about {topic}."),
    ("human", "Tell me {joke_count} jokes."),
]

prompt_template = ChatPromptTemplate.from_messages(messages)
prompt = prompt_template.invoke({"topic": "lawyers", "joke_count": 3})
result = llm.invoke(prompt)
print(result)