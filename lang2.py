from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
load_dotenv()
llm = init_chat_model(model="llama-3.1-8b-instant", temperature=0, model_provider="groq" )
response = llm.invoke("give me a fun fact")
print(response.content) 