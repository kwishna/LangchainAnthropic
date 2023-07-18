from langchain.chat_models import ChatAnthropic
from langchain.memory import ConversationBufferMemory
from langchain.agents import Tool, AgentType
from langchain.agents import initialize_agent
from langchain.tools import DuckDuckGoSearchRun
import os

os.environ['ANTHROPIC_API_KEY'] = 'Anthropic Key'

memory = ConversationBufferMemory(memory_key='chat_history',
                                  return_messages=True)
llm = ChatAnthropic(model='claude-2', temperature=0.7)
search = DuckDuckGoSearchRun()

tools = [
  Tool(
    name='Current Search',
    func=search.run,
    description=
    "useful for when you need to answer questions about current events or the current state of the world"
  ),
]

agent_chain = initialize_agent(
  tools=tools,
  llm=llm,
  agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION,
  memory=memory)

print(agent_chain.run(input="Hi, I am human."))
print(agent_chain.run(input="What is Elon musk's X.ai?"))
print(agent_chain.run(input="What do they plan to do?"))
