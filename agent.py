from dotenv import load_dotenv
import os

from langchain_openai import AzureChatOpenAI
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.agents import AgentExecutor, create_openai_functions_agent
from langchain.agents.format_scratchpad import format_to_openai_function_messages
from langchain.agents.output_parsers import OpenAIFunctionsAgentOutputParser
from langchain.memory import ConversationBufferWindowMemory
from langchain.tools import tool

# 1. Load environment variables
load_dotenv()


# Initialize Azure LLM
llm = AzureChatOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    deployment_name=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
    api_version="2024-08-01-preview",   # latest stable API version
)
# 3. Add a simple tool (calculator)
@tool
def add_numbers(a: int, b: int) -> int:
    """Adds two numbers and returns the result."""
    return a + b

tools = [add_numbers]

# 4. Setup Memory
memory = ConversationBufferWindowMemory(memory_key="chat_history", k=5, return_messages=True)

# 5. Define Prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant that remembers context of the conversation."),
    MessagesPlaceholder(variable_name="chat_history"),
    ("user", "{input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad")
])

# 6. Create Agent
agent = create_openai_functions_agent(
    llm=llm,
    prompt=prompt,
    tools=tools
)
# 7. Agent Executor with tools + memory
agent_executor = AgentExecutor(agent=agent, tools=tools, memory=memory, verbose=True)

# 8. Run interaction loop
if __name__ == "__main__":
    print("Chat with your Azure OpenAI agent. Type 'exit' to quit.\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        response = agent_executor.invoke({"input": user_input})
        print("Agent:", response["output"])
