from dotenv import load_dotenv  
from pydantic import BaseModel
from langchain_groq import ChatGroq     
load_dotenv()
llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0)
class llm_schema(BaseModel):
    setup: str
    punchline: str  

llm_structured_output=llm.with_structured_output(llm_schema )
response=llm_structured_output.invoke("tell me a joke")
print(response) 