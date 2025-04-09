from langchain_community.llms import Ollama
from langchain_core.prompts import PromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain import hub
from langchain.agents import create_react_agent, AgentExecutor
from langchain.agents import tool
import datetime

# Tool with docstring that tells the agent how to use the format argument
@tool
def get_system_time(format: str = "%Y-%m-%d %H:%M:%S"):
    """Returns the current system time. You can specify a 'format' string like '%H:%M:%S' for hours, minutes, and seconds."""
    current_time = datetime.datetime.now()
    return current_time.strftime(format)

# Load LLaMA 3 via Ollama
llm = Ollama(model="llama3")

# Define the query
query = "What is the current time in London (you are in India)? Just show the current time (like 14:23:05) and not the date. Use the format '%H:%M:%S'."

# Load the ReAct prompt template
prompt_template = hub.pull("hwchase17/react")

# Register the tools
tools = [get_system_time]

# Create the agent and executor
agent = create_react_agent(llm, tools, prompt_template)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# Run the agent
agent_executor.invoke({"input": query})