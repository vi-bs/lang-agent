from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnableLambda, RunnableSequence
from langchain_community.llms import Ollama

# Initialize the Ollama LLaMA 3 model
model = Ollama(model="llama3")

# Define the chat prompt template
prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You love facts and you tell facts about {animal}"),
        ("human", "Tell me {count} facts."),
    ]
)

# Define the steps in the pipeline
format_prompt = RunnableLambda(lambda x: prompt_template.format_prompt(**x))
invoke_model = RunnableLambda(lambda x: model.invoke(x.to_messages()))
parse_output = RunnableLambda(lambda x: x)

# Combine into a sequence
chain = RunnableSequence(first=format_prompt, middle=[invoke_model], last=parse_output)

# Run the chain
response = chain.invoke({"animal": "cat", "count": 2})

# Output the response
print(response)