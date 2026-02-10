from dotenv import load_dotenv
load_dotenv()   
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
llm= ChatGroq(model="llama-3.1-8b-instant",temperature=0)
user_input=input("Enter your query: ")
user_tone=input("Enter the tone you want the response in: ")
prompt_template=ChatPromptTemplate.from_messages([
    ("system","you are a {tone} person"),
    ("user","give a fun fact about {topic}"),
])
promt_given=prompt_template.invoke({"tone":user_tone,"topic":user_input})
response = llm.invoke(promt_given)  
print(response.content) 