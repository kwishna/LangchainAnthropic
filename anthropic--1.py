from langchain.chat_models import ChatAnthropic
from langchain.schema import AIMessage, HumanMessage, SystemMessage
import os

os.environ['ANTHROPIC_API_KEY'] = 'Anthropic Key'

chat = ChatAnthropic(model='claude-2',
                     anthropic_api_key=os.environ['ANTHROPIC_API_KEY'])

messages = [
  SystemMessage(content='You are an helpful AI assistant'),
  HumanMessage(content='How do you compare to gpt-4?'),
  AIMessage(content='Do you want the comparision in tabular format?'),
  HumanMessage(content='Yes, please show the comparision in tabular format?'),
]

print(chat(messages))
