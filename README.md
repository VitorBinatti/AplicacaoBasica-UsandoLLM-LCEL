# README - Projeto de Tradução utilizando LangChain e GROQ

## Índice

1. [Descrição do Projeto](#descrição-do-projeto)
2. [Tecnologias Utilizadas](#tecnologias-utilizadas)
3. [Estrutura do Repositório](#estrutura-do-repositório)
4. [Instalação](#instalação)
    - [Clone do Repositório](#clone-do-repositório)
    - [Instalação das Dependências](#instalação-das-dependências)
5. [Explicação do Código](#explicação-do-código)
    - [1. Importação das Bibliotecas](#1-importação-das-bibliotecas)
    - [2. Carregamento das Variáveis de Ambiente](#2-carregamento-das-variáveis-de-ambiente)
    - [3. Criando o Modelo GROQ](#3-criando-o-modelo-groq)
    - [4. Parser de Saída](#4-parser-de-saída)
    - [5. Prompt Template](#5-prompt-template)
    - [6. Chain](#6-chain)
    - [7. Execução da Chain](#7-execução-da-chain)
6. [Glossário](#glossário)

## Descrição do Projeto

Este projeto tem como objetivo realizar a tradução de uma frase para o idioma especificado utilizando o modelo de linguagem Gemma2-9b-It da API GROQ. A solução é baseada na biblioteca LangChain, que facilita a construção de fluxos de trabalho em IA, permitindo a integração de vários componentes como modelos de linguagem, prompts e parsers de saída.

## Tecnologias Utilizadas

- **LangChain**: Biblioteca para construção de fluxos de trabalho com modelos de linguagem.
- **GROQ**: Plataforma de modelos de linguagem para tarefas como tradução, geração de texto, etc.
- **Python-dotenv**: Carregamento de variáveis de ambiente a partir de arquivos `.env`.
- **API Key do GROQ**: Necessária para autenticar a utilização da API do GROQ.
  
## Estrutura do Repositório

```
/meu_projeto
  ├── .env                 # Arquivo para variáveis de ambiente
  ├── requirements.txt      # Arquivo com dependências do projeto
  ├── main.py               # Arquivo com o código do projeto
  ├── README.md             # Este arquivo
```

## Instalação

### Clone do Repositório

Para começar, clone o repositório para a sua máquina local. Abra o terminal e execute o comando abaixo:

```bash
git clone <URL_DO_REPOSITORIO>
```

Substitua `<URL_DO_REPOSITORIO>` pelo link do repositório.

### Instalação das Dependências

Instale as dependências necessárias do projeto utilizando o arquivo `requirements.txt`. Execute o comando abaixo dentro da pasta do projeto:

```bash
pip install -r requirements.txt
```

## Explicação do Código

### 1. Importação das Bibliotecas

```python
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from dotenv import load_dotenv, find_dotenv
import os
```

Aqui estamos importando as bibliotecas necessárias para nosso projeto:

- **LangChain**: Para criação de templates de prompts e manipulação de mensagens.
- **GROQ**: Para utilizar o modelo de linguagem da API GROQ.
- **dotenv**: Para carregar variáveis de ambiente a partir do arquivo `.env`.
- **os**: Para manipulação de variáveis de ambiente diretamente no código.

### 2. Carregamento das Variáveis de Ambiente

```python
load_dotenv(find_dotenv())
groq_api_key = os.getenv("GROQ_API_KEY")
```

Neste bloco, estamos carregando as variáveis de ambiente do arquivo `.env` usando `dotenv`. Em seguida, a chave da API do GROQ é recuperada através de `os.getenv()`.

### 3. Criando o Modelo GROQ

```python
llm = ChatGroq(
    model="Gemma2-9b-It",  # escolha do modelo de API utilizado
    groq_api_key=groq_api_key,  # chave de API do GROQ
)
```

Aqui, estamos configurando o modelo de linguagem do GROQ. O modelo `Gemma2-9b-It` é o escolhido para este exemplo, e passamos a chave da API carregada anteriormente para autenticação.

### 4. Parser de Saída

```python
parser = StrOutputParser()
```

O parser de saída é configurado para converter a resposta gerada pelo modelo em uma string simples. Ele é necessário para que possamos tratar a saída do modelo de forma que ela seja útil para o próximo passo do processo.

### 5. Prompt Template

```python
generic_template = "Traduza a seguinte frase em {language}"

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", generic_template),
        ("user", "{text}")
    ]
)
```

Aqui, estamos criando um template de prompt para a tradução de frases. O prompt solicita ao sistema que traduza o texto para o idioma especificado pela variável `{language}`, e o texto a ser traduzido é passado pela variável `{text}`.

### 6. Chain

```python
chain = prompt | llm | parser
```

Uma *chain* (cadeia) é uma sequência de componentes que são executados em ordem. Neste caso, a cadeia inclui o prompt, o modelo de linguagem do GROQ e o parser de saída. O símbolo `|` é utilizado para encadear os componentes em LangChain.

### 7. Execução da Chain

```python
print(chain.invoke({'language': 'German', 'text': 'bom dia'}))
```

Por fim, executamos a *chain* com a frase "bom dia" para ser traduzida para o idioma "Alemão". O resultado da tradução será impresso no terminal.

## Glossário

- **LangChain**: Biblioteca que facilita a construção de fluxos de trabalho para IA, integrando diferentes componentes como modelos de linguagem, prompts, e parsers.
- **GROQ**: Plataforma que oferece modelos de linguagem para realizar tarefas de NLP, como tradução, resposta a perguntas, entre outros.
- **API Key**: Uma chave utilizada para autenticação ao acessar serviços de API, como o GROQ.
- **Prompt Template**: Template usado para formatar as instruções enviadas ao modelo de linguagem.
- **Parser**: Componente que interpreta e converte a saída do modelo em um formato utilizável.
- **Chain**: Sequência de componentes encadeados para processar um fluxo de dados em ordem.

Com isso, você tem uma visão geral e detalhada sobre como o código funciona e como configurar seu ambiente para rodar este projeto.