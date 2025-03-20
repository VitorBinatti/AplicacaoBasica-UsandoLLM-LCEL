# importação das bibliotecas
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from dotenv import load_dotenv, find_dotenv
import os

#carregando as variáveis de ambiente
load_dotenv(find_dotenv())
groq_api_key = os.getenv("GROQ_API_KEY")

#1. criando o modelo GROQ
llm = ChatGroq (
    model = "Gemma2-9b-It", #escolha do modelo de API utilizado
    groq_api_key = groq_api_key, #chave de API do GROQ
) 


#2. PARSER de saída : isso é necessário para que o sistema entenda a saída do modelo
parser = StrOutputParser()

#3. prompt template: usando LCEL - Chain the components
generic_template = "Traduza o seguinte texto em {language}"

prompt = ChatPromptTemplate.from_messages(
    [
        {"system", generic_template},
        {"user", "(text)"}
    ]
)

#O que é uma chain? Uma cadeia é uma sequência de componentes que são executados todos em ordem

#4. Chain
chain = prompt | llm | parser

#5. executar a chain
print(chain.invoke({'language':'German', 'text':'hello'}))


#Criar o prompt (basico) ***** estudar sobre o prompt engineering (few-shot, zero-shot, one-shot, chain of thoughts)
#messages = [
#    SystemMessage(content="Traduza o seguinte texto do português para o inglês"),
#    HumanMessage(content="Tudo bem? Como você está?")
#]


#serve para testar o resultado da aplicação
#result = llm.invoke(messages)
#print(result)  