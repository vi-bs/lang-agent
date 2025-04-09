from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnableLambda, RunnableParallel
from langchain.schema.output_parser import StrOutputParser
from langchain_community.llms import Ollama

# Initialize Ollama with the LLaMA 3 model
model = Ollama(model="llama3")

# Define the prompt template for the movie summary
summary_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a movie critic."),
        ("human", "Provide a brief summary of the movie {movie_name}."),
    ]
)

# Define plot analysis prompt generator
def analyze_plot(plot):
    plot_template = ChatPromptTemplate.from_messages(
        [
            ("system", "You are a movie critic."),
            ("human", "Analyze the plot: {plot}. What are its strengths and weaknesses?"),
        ]
    )
    return plot_template.format_prompt(plot=plot)

# Define character analysis prompt generator
def analyze_characters(characters):
    character_template = ChatPromptTemplate.from_messages(
        [
            ("system", "You are a movie critic."),
            ("human", "Analyze the characters: {characters}. What are their strengths and weaknesses?"),
        ]
    )
    return character_template.format_prompt(characters=characters)

# Combine both analyses into a single verdict
def combine_verdicts(plot_analysis, character_analysis):
    return f"Plot Analysis:\n{plot_analysis}\n\nCharacter Analysis:\n{character_analysis}"

# Define individual branches for plot and character analysis
plot_branch_chain = (
    RunnableLambda(lambda x: analyze_plot(x)) | model | StrOutputParser()
)

character_branch_chain = (
    RunnableLambda(lambda x: analyze_characters(x)) | model | StrOutputParser()
)

# Full chain using LangChain Expression Language (LCEL)
chain = (
    summary_template
    | model
    | StrOutputParser()
    | RunnableParallel(branches={"plot": plot_branch_chain, "characters": character_branch_chain})
    | RunnableLambda(lambda x: combine_verdicts(x["branches"]["plot"], x["branches"]["characters"]))
)

# Run the chain
result = chain.invoke({"movie_name": "Inception"})

# Output the result
print(result)