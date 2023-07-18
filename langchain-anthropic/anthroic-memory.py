from langchain.chat_models import ChatAnthropic
from langchain.memory import ConversationBufferMemory
from langchain.agents import Tool, AgentType
from langchain.agents import initialize_agent
from langchain.tools import DuckDuckGoSearchRun
import os

os.environ['ANTHROPIC_API_KEY'] = 'Anthropic API Key'

memory = ConversationBufferMemory(memory_key='chat_history',
                                  return_messages=True)

llm = ChatAnthropic(model='claude-2', temperature=0.7)
search = DuckDuckGoSearchRun()

tools = [
  Tool(
    name='Duckduckgo Search Engine Internet Access',
    func=search.run,
    description=
    "To fetch information from internet to have the access to all the data available on the internet till today."
  ),
]

agent_chain = initialize_agent(
  tools=tools,
  llm=llm,
  agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION,
  memory=memory)

print(agent_chain.run(input="Hi, I am human."))
print(agent_chain.run(input="Why does governments are not concerned to uncontrolled rapid AI development? How does it going to benefit big businesses?"))
print(agent_chain.run(input="how the education system is going to change in the future?"))
