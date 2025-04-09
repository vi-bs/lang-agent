from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnableLambda
from langchain_community.llms import Ollama

# Initialize the Ollama model (LLaMA 3)
model = Ollama(model="llama3")

# Define a prompt template for generating animal facts
animal_facts_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You like telling facts and you tell facts about {animal}."),
        ("human", "Tell me {count} facts."),
    ]
)

# Define a prompt template for translating to a different language
translation_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a translator and convert the provided text into {language}."),
        ("human", "Translate the following text to {language}: {text}"),
    ]
)

# Additional processing steps using RunnableLambda
count_words = RunnableLambda(lambda x: f"Word count: {len(x.split())}\n{x}")
prepare_for_translation = RunnableLambda(lambda output: {"text": output, "language": "french"})

# Build the full chain using LCEL
chain = (
    animal_facts_template
    | model
    | StrOutputParser()
    | prepare_for_translation
    | translation_template
    | model
    | StrOutputParser()
)

# Run the chain
result = chain.invoke({"animal": "cat", "count": 2})

# Output the result
print(result)