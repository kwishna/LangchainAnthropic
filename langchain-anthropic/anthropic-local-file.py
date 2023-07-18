from langchain.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatAnthropic
from langchain.document_loaders import TextLoader, DirectoryLoader
from langchain.embeddings import HuggingFaceInstructEmbeddings
import os

os.environ['ANTHROPIC_API_KEY'] = 'Anthropic Key'

loader = DirectoryLoader("./dir",
                         glob='./*.txt',
                         loader_cls=TextLoader)
documents = loader.load()
len(documents)

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000,
                                               chunk_overlap=200)
texts = text_splitter.split_documents(documents)

instructor_embeddings = HuggingFaceInstructEmbeddings(
  model_name='hkunlp/instructor-xl', model_kwargs={"device": "cuda"})

persist_directory = 'db'
embedding = instructor_embeddings

vectordb = Chroma.from_documents(documents=texts,
                                 embedding=embedding,
                                 persist_directory=persist_directory)

retriever = vectordb.as_retriever(search_kwargs={"k": 7})

llm = ChatAnthropic(temperature=0.0)

qa_chain = RetrievalQA.from_chain_type(llm=llm,
                                       chain_type='stuff',
                                       retriever=retriever,
                                       return_source_documents=True)

query = "What did Elon announce?"
llm_response = qa_chain(query)
print(llm_response['result'])

query = "Who is on the team?"
llm_response = qa_chain(query)
print(llm_response['result'])

query = "Who is he going to call his GPT model?"
llm_response = qa_chain(query)
print(llm_response['result'])

query = "What is going to be CEO?"
llm_response = qa_chain(query)
print(llm_response['result'])

query = "What did Elon musk said about China and AI?"
llm_response = qa_chain(query)
print(llm_response['result'])