import os
import dotenv
from fastapi import FastAPI
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage,SystemMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

from langserve import add_routes


dotenv.load_dotenv()

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

from langchain_groq import ChatGroq

model = ChatGroq(model="llama-3.1-8b-instant", temperature=0.7,groq_api_key=os.getenv("GROQ_API_KEY"))


from langchain_core.messages import HumanMessage,SystemMessage
messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="What is the capital of France?"),
]


from langchain_core.output_parsers import StrOutputParser
parser = StrOutputParser()


from langchain_core.prompts import ChatPromptTemplate

generic_prompt = ChatPromptTemplate.from_messages(
    [
       ("system", "You are a helpful assistant."),
       ("human", "{text}")
    ]
)


    
chain =generic_prompt | model | parser
chain.invoke({"text":"what is Artificial Intelligence?"})



app = FastAPI(title="Groq API", description="API for Groq LLMs using LangServe",version="1.0.0"
              )

add_routes(
    app,
    chain,
    path="/groq",
)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)




