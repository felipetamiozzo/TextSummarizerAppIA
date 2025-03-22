from langchain_groq import ChatGroq # Import corrigido
from langchain.docstore.document import Document  # Importa a classe Document da biblioteca langchain.docstore.document
from langchain.text_splitter import CharacterTextSplitter  # Importa a classe CharacterTextSplitter da biblioteca langchain.text_splitter
from langchain.chains.summarize import load_summarize_chain  # Importa a função load_summarize_chain da biblioteca langchain.chains.summarize
from dotenv import load_dotenv, find_dotenv  # Importa as funções load_dotenv e find_dotenv da biblioteca dotenv
import os  # Importa a biblioteca os para interagir com variáveis de ambiente

# Carregar variáveis de ambiente
load_dotenv(find_dotenv())
GROQ_API_KEY = os.environ["GROQ_API_KEY"]

# Criar o modelo AI com Groq
llm = ChatGroq(
    model="llama-3.3-70b-versatile",  
    temperature=1,
    groq_api_key=GROQ_API_KEY
)

text = ("O Brasil é um país localizado na América do Sul, sendo o quinto maior país do mundo em área territorial. "
        "É uma república federativa presidencialista, formada pela união de 26 estados federados e por um distrito federal. "
        "A capital do Brasil é Brasília e a cidade mais populosa é São Paulo. A língua oficial do Brasil é o português e a moeda é o real. "
        "O Brasil é um país com uma grande diversidade cultural e é conhecido por suas belezas naturais, como as praias, a floresta amazônica e as cachoeiras. "
        "A economia do Brasil é uma das maiores do mundo e é baseada na agricultura, na indústria e nos serviços. "
        "A hiperautomação transforma empresas ao otimizar os processos de negócios, eliminando tarefas repetitivas e automatizando as manuais. "
        "Isso traz vários benefícios importantes.")

# SPLIT TEXT: Dividir o texto em partes menores
text_splitter = CharacterTextSplitter()
texts = text_splitter.split_text(text)

# Criar Documentos a partir dos pedaços de texto
docs = [Document(page_content=chunk) for chunk in texts]

# Carregar a cadeia de sumarização
chain = load_summarize_chain(llm=llm, chain_type="stuff")

# Executa a cadeia de sumarização e exibe o resumo
summary = chain.invoke(docs)
print(summary['output_text'])