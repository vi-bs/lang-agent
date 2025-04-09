from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnableBranch
from langchain_community.llms import Ollama

# Initialize the Ollama model (LLaMA 3)
model = Ollama(model="llama3")

# Prompt templates for each sentiment type
positive_feedback_template = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("human", "Generate a thank you note for this positive feedback: {feedback}."),
])

negative_feedback_template = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("human", "Generate a response addressing this negative feedback: {feedback}."),
])

neutral_feedback_template = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("human", "Generate a request for more details for this neutral feedback: {feedback}."),
])

escalate_feedback_template = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("human", "Generate a message to escalate this feedback to a human agent: {feedback}."),
])

# Classification template to determine sentiment
classification_template = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("human", "Classify the sentiment of this feedback as positive, negative, neutral, or escalate: {feedback}."),
])

# Chain for classifying sentiment
classification_chain = classification_template | model | StrOutputParser()

# Branching logic for feedback response generation
branches = RunnableBranch(
    (
        lambda x: "positive" in x.lower(),
        positive_feedback_template | model | StrOutputParser()
    ),
    (
        lambda x: "negative" in x.lower(),
        negative_feedback_template | model | StrOutputParser()
    ),
    (
        lambda x: "neutral" in x.lower(),
        neutral_feedback_template | model | StrOutputParser()
    ),
    escalate_feedback_template | model | StrOutputParser()
)

# Final combined chain
chain = classification_chain | branches

# Example feedback input
review = "The product is terrible. It broke after just one use and the quality is very poor."
result = chain.invoke({"feedback": review})

# Output the result
print(result)